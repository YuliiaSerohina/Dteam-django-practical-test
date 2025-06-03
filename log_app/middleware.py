from .models import RequestLog
import json


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    return x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')


def logging_middleware(get_response):
    def middleware(request):
        response = get_response(request)
        RequestLog.objects.create(
            method=request.method,
            path=request.path,
            query_params=json.dumps(request.GET.dict()),
            ip_address=get_client_ip(request),
            response_code=response.status_code
        )
        return response
    return middleware
