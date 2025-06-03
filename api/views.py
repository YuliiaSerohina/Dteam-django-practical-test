from django.shortcuts import render, redirect
from main.models import CV
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from api.serializers import CVSerializer


def api_page(request):
    return render(request, 'api_page.html')


@api_view(['GET', 'POST'])
def cv_get_post(request):
    if request.method == 'POST':
        serializer = CVSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    cv_all_list = CV.objects.all()
    serializer = CVSerializer(cv_all_list, many=True)
    return Response(serializer.data)


def get_cv_id(request):
    if request.method == 'POST':
        cv_id = request.POST.get('cv_id')
        if cv_id:
            return redirect('cv_delete_put', id_cv=cv_id)
    cv_ids = CV.objects.values_list('id', flat=True)
    return render(request, 'get_cv_id.html', {'cv_ids': cv_ids})


@api_view(['GET', 'PUT', 'DELETE'])
def cv_delete_put(request, id_cv):
    cv = CV.objects.get(id=id_cv)
    if request.method == 'PUT':
        serializer = CVSerializer(cv, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        cv.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    serializer = CVSerializer(cv)
    return Response(serializer.data)
