from django.urls import path
from .views import AreaListView, SubjectListView


app_name = 'subjects'

urlpatterns = [
    path('area-list/', AreaListView.as_view(), name='area-list'),
    path('subject-list/', SubjectListView.as_view(), name='subject-list'),
#    path('package-create/', PackageCreateView.as_view(), name='package-create'),
]