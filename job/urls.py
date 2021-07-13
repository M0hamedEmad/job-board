from django.urls import path
from . import views
from . import api
app_name = 'job'

urlpatterns = [
    path('', views.job_list, name='jobs'),
    path('add', views.post_job, name='post_job'),
    path('<str:slug>', views.job_detail, name='job_detail'),
    path('api/', api.JobApi.as_view(), name='joblistapi'),
    path('api/<int:id>', api.job, name='apijob')
]