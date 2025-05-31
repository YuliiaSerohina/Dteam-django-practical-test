from django.urls import path
import main.views

urlpatterns = [
    path('', main.views.main_page)
]
