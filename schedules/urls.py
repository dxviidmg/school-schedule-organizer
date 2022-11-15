from django.urls import path
from . import views


app_name = 'schedules'

urlpatterns = [
    path('schoolperiod-list/', views.SchoolPeriodListView.as_view(), name='schoolperiod-list'),
    path('schoolperiod-create/', views.SchoolPeriodCreateView.as_view(), name='schoolperiod-create'),    
    path('schoolperiod-detail/<int:pk>/', views.SchoolPeriodDetailView.as_view(), name='schoolperiod-detail'),
    path('group-detail/<int:pk>/', views.GroupDetailView.as_view(), name='group-detail'),
    path('class-update/<int:pk>/', views.ClassUpdateView.as_view(), name='class-update'),
    path('schedule-create/<int:pk>/', views.ScheduleCreateView.as_view(), name='schedule-create'),
]