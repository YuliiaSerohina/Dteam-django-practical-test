from django.urls import path
import main.views

urlpatterns = [
    path('', main.views.main_page, name='main_page'),
    path('<int:cv_id>/', main.views.cv_details, name='cv_details'),
    path('<int:cv_id>/download_pdf/', main.views.cv_pdf_download, name='cv_pdf_download'),
    path('api/', main.views.api_page, name='api_page'),
    path('api/get_post/', main.views.cv_get_post, name='cv_get_post'),
    path('api/cv_get_put_delete/', main.views.cv_get_put_delete, name='cv_get_put_delete')

]
