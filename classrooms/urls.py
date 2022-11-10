from django.urls import path
from . import views


app_name = 'classrooms'

urlpatterns = [
    path('classroom-list/', views.ClassroomListView.as_view(), name='classroom-list'),
    path('classroom-create/', views.ClassroomCreateView.as_view(), name='classroom-create'),    
]