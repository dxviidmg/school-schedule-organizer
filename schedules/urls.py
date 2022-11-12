from django.urls import path
from . import views


app_name = 'schedules'

urlpatterns = [
    path('schoolperiod-list/', views.SchoolPeriodListView.as_view(), name='schoolperiod-list'),
    path('schoolperiod-create/', views.SchoolPeriodCreateView.as_view(), name='schoolperiod-create'),    
]