from django.urls import path
from . import views




urlpatterns = [
    path('assign-role/', views.assign_role_view, name='assign_role'),
]
