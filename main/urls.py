from django.urls import path
import main.views

urlpatterns = [
    path('', main.views.main_page, name='main_page'),
    path('<int:cv_id>/', main.views.cv_details, name='cv_details'),

]
