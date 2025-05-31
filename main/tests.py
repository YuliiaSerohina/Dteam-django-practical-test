from django.test import TestCase
from django.urls import reverse
from .models import CV


class CVViewsTestCase(TestCase):
    def setUp(self):
        self.cv = CV.objects.create(
            first_name="User",
            last_name="Test",
            skills="C++, Java",
            projects="Project_test",
            bio="User for test",
            contacts="test@test.com"
        )

    def test_main_page_view(self):
        """
        Test that the main page loads successfully,
        displays the full name of the CV, and uses the correct template.
        """
        response = self.client.get(reverse('main_page'))
        self.assertEqual(response.status_code, 200)
        expected_name = f"{self.cv.first_name} {self.cv.last_name}"
        self.assertContains(response, expected_name)
        self.assertTemplateUsed(response, 'main_page.html')

    def test_cv_detail_view(self):
        """
        Test that the detail view for a single CV loads correctly,
        contains the last name of the CV, and uses the 'cv_details.html' template.
        """
        response = self.client.get(reverse('cv_details', args=[self.cv.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.cv.last_name)
        self.assertTemplateUsed(response, 'cv_details.html')
