from django.urls import path
import api.views

urlpatterns = [
    path('', api.views.api_page, name='api_page'),
    path('get_post/', api.views.cv_get_post, name='cv_get_post'),
    path('get_cv_id/', api.views.get_cv_id, name='get_cv_id'),
    path('<int:id_cv>/delete_put/', api.views.cv_delete_put, name='cv_delete_put'),

]
