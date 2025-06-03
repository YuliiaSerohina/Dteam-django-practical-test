from django.urls import path
import log_app.views

urlpatterns = [
    path('logs/', log_app.views.show_logs, name='logs'),
]