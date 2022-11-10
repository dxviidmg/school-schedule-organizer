from django.urls import path
from . import views


app_name = 'subjects'

urlpatterns = [
    path('area-list/', views.AreaListView.as_view(), name='area-list'),
    path('area-create/', views.AreaCreateView.as_view(), name='area-create'),
    path('subject-list/', views.SubjectListView.as_view(), name='subject-list'),
    path('subject-create/', views.SubjectCreateView.as_view(), name='subject-create'),
    path('subject-detail/<int:pk>/', views.SubjectDetailView.as_view(), name='subject-detail'),
]