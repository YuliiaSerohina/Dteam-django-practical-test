from django.urls import path
import main.views

urlpatterns = [
    path('', main.views.main_page, name='main_page'),
    path('<int:cv_id>/', main.views.cv_details, name='cv_details'),
    path('<int:cv_id>/download_pdf/', main.views.cv_pdf_download, name='cv_pdf_download'),
    path('settings/', main.views.settings_view, name='settings_view'),
    path('<int:cv_id>/translation/', main.views.translate_cv_view, name='translate_cv_view'),

]
