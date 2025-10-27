from django.urls import path
from .views import ManagerIndex, ManagerDetails

urlpatterns = [
    path('managers/', ManagerIndex.as_view(), name='manager_path'),
    path('managers/<int:manager_id>', ManagerDetails.as_view(), name='manager_path'),

]
