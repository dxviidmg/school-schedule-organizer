from . import views
from django.urls import path

app_name = 'teachers'

urlpatterns = [
    path('teacher-suggestion/', views.TeacherSuggestion.as_view(), name='teacher-suggestion'),
]