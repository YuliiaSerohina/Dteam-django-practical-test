from django.shortcuts import render
from .models import CV


def main_page(request):
    cv_all_list = CV.objects.only("first_name", "last_name", "skills")
    return render(request, 'main_page.html', {"cv_all_list": cv_all_list})


def cv_details(request, cv_id):
    cv_get = CV.objects.filter(id=cv_id)
    return render(request, 'cv_details.html', {"cv_get": cv_get})

