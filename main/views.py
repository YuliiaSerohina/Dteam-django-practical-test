from django.shortcuts import render
from .models import CV
from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa


def main_page(request):
    cv_all_list = CV.objects.only("first_name", "last_name", "skills")
    return render(request, 'main_page.html', {"cv_all_list": cv_all_list})


def cv_details(request, cv_id):
    cv = CV.objects.get(id=cv_id)
    return render(request, 'cv_details.html', {"cv": cv})


def cv_pdf_download(request, cv_id):
    cv = CV.objects.get(id=cv_id)
    html_string = render_to_string('cv_details.html', {"cv": cv})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{cv.first_name}_{cv.last_name}_CV.pdf"'
    pisa_status = pisa.CreatePDF(src=html_string, dest=response)
    if pisa_status.err:
        return HttpResponse('Error', status=500)
    return response
