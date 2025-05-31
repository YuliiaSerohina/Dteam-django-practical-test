from django.shortcuts import render
from .models import CV


def main_page(request):
    cv_all_list = CV.objects.only("first_name", "last_name", "skills")
    return render(request, 'main_page.html', {"cv_all_list": cv_all_list})


