from .views import SectionsHome, SchoolProfileView
from django.urls import path, include


app_name = 'schoolinfo'

urlpatterns = [
    path('', SectionsHome.as_view(), name='sections_home'),
    path('school-profile', SchoolProfileView.as_view(), name='school_profile'),
    
]