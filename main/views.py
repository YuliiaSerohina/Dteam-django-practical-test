from django.shortcuts import render
from .models import CV
from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CVSerializer


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


def api_page(request):
    cvs = CV.objects.all()
    return render(request, 'api_page.html', {"cvs": cvs})


@api_view(['GET', 'POST'])
def cv_get_post(request):
    if request.method == 'GET':
        cvs = CV.objects.all()
        serializer = CVSerializer(cvs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CVSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def cv_get_put_delete(request):
    if request.method == 'GET':
        cvs = CV.objects.all()
        serializer = CVSerializer(cvs, many=True)
        return Response(serializer.data)

    cv_id = request.data.get('id')
    if not cv_id:
        return Response({'error': 'ID is required for PUT and DELETE'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        cv = CV.objects.get(id=cv_id)
    except CV.DoesNotExist:
        return Response({'error': 'CV not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = CVSerializer(cv, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cv.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)