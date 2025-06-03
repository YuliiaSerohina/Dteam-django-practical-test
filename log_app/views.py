from django.shortcuts import render
from .models import RequestLog


def show_logs(request):
    logs = RequestLog.objects.all().order_by('-timestamp')[:10]
    return render(request, 'logs.html', {'logs': logs})
