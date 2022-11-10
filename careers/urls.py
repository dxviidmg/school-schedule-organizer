from django.urls import path
from . import views


app_name = 'careers'

urlpatterns = [
    path('career-list/', views.CareerListView.as_view(), name='career-list'),
    path('career-create/', views.CareerCreateView.as_view(), name='career-create'),
]