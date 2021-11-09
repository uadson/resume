from django.urls import path

from .views import ResumeView


app_name = 'resume'

urlpatterns = [
    # Home Page
    path('', ResumeView.as_view(), name='index'),
]
