from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from main.models import CV


class CVTests(APITestCase):
    def setUp(self):
        self.cv = CV.objects.create(
            first_name="User",
            last_name="Test",
            skills="C++, Java",
            projects="Project_test",
            bio="User for test",
            contacts="test@test.com"
        )

    def test_post_cv(self):
        url = reverse('cv_get_post')
        data = {
            'first_name': 'Anna',
            'last_name': 'Hana',
            'skills': 'JavaScript'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CV.objects.count(), 2)

    def test_get_cv_list(self):
        url = reverse('cv_get_post')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_cv(self):
        url = reverse('cv_delete_put', args=[self.cv.id])
        self.assertEqual(CV.objects.get(id=self.cv.id).first_name, 'User')
        data = {
            'first_name': 'Anna',
            'last_name': 'Test',
            'skills': 'C++, Java',
            'projects': 'Project_test',
            'bio': 'User for test',
            'contacts': 'test@test.com'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(CV.objects.get(id=self.cv.id).first_name, 'Anna')

    def test_delete_cv(self):
        url = reverse('cv_delete_put', args=[self.cv.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(CV.objects.count(), 0)
