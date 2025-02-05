from django.urls import path
from django.contrib import admin
from django.http import HttpResponse
from .views import get_user_roles, assign_user_role, api_login_view, hiring_manager_dashboard  # Import the views

# Define the test and home views
def test_view(request):
    return HttpResponse("Test page is working!")

def home_view(request):
    return HttpResponse("Welcome to the Candidate Screening App!")

# Define the URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),  # Root URL
    path('test/', test_view, name='test'),  # Test URL

    # API URLs
    path('api/get-user-roles/', get_user_roles, name='get_user_roles'),  # Added get_user_roles API
    path('api/assign-user-role/', assign_user_role, name='assign_user_role'),
    path('api/login/', api_login_view, name='api_login'),  # New login API route

    # Role-based dashboards (ensure these views are protected)
    path('hiring-manager/dashboard/', hiring_manager_dashboard, name='hiring_manager_dashboard'),  # Protected dashboard
]
