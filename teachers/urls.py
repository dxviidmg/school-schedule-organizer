from . import views
from django.urls import path

app_name = 'teachers'

urlpatterns = [
    path('teacher-list/', views.TeacherListView.as_view(), name='teacher-list'),    
    path('teacher-detail/<int:pk>/', views.TeacherDetailView.as_view(), name='teacher-detail'),
    path('teacher-suggestion/', views.TeacherSuggestion.as_view(), name='teacher-suggestion'),
    path('teacher-create/', views.TeacherCreationView.as_view(), name='teacher-create'),
    
]