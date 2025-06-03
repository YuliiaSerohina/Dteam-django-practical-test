from django.test import TestCase, RequestFactory
from django.http import HttpResponse
from .models import RequestLog
from .middleware import logging_middleware, get_client_ip
import json


class RequestLogModelTest(TestCase):
    def test_create_request_log(self):
        log = RequestLog.objects.create(
            method="GET",
            path="/test-path",
            query_params=json.dumps({"param": "value"}),
            ip_address="127.0.0.1",
            response_code=200
        )
        self.assertEqual(log.method, "GET")
        self.assertEqual(log.path, "/test-path")
        self.assertEqual(json.loads(log.query_params), {"param": "value"})
        self.assertEqual(log.ip_address, "127.0.0.1")
        self.assertEqual(log.response_code, 200)
        self.assertIsNotNone(log.timestamp)

    def test_str_representation(self):
        log = RequestLog.objects.create(
            method="POST",
            path="/another-path",
            ip_address="192.168.1.1",
            response_code=404
        )
        self.assertIn("POST /another-path", str(log))


class GetClientIpTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_get_client_ip_with_x_forwarded_for(self):
        request = self.factory.get('/')
        request.META = {'HTTP_X_FORWARDED_FOR': '192.168.1.1, 10.0.0.1'}
        self.assertEqual(get_client_ip(request), '192.168.1.1')

    def test_get_client_ip_with_remote_addr(self):
        request = self.factory.get('/')
        request.META = {'REMOTE_ADDR': '127.0.0.1'}
        self.assertEqual(get_client_ip(request), '127.0.0.1')


class LoggingMiddlewareTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_middleware_creates_log(self):
        def dummy_view(request):
            return HttpResponse("OK", status=200)

        request = self.factory.get('/test-path?foo=bar', HTTP_X_FORWARDED_FOR='10.0.0.1')
        middleware = logging_middleware(dummy_view)
        response = middleware(request)

        self.assertEqual(response.status_code, 200)

        logs = RequestLog.objects.all()
        self.assertEqual(logs.count(), 1)

        log = logs.first()
        self.assertEqual(log.method, 'GET')
        self.assertEqual(log.path, '/test-path')
        self.assertEqual(json.loads(log.query_params), {'foo': 'bar'})
        self.assertEqual(log.ip_address, '10.0.0.1')
        self.assertEqual(log.response_code, 200)

