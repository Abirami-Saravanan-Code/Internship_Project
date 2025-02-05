# In api/urls.py
# from django.urls import path
# from .views import CandidateListCreateView, CandidateDetailView

# urlpatterns = [
#     path('candidates/', CandidateListCreateView.as_view(), name='candidate-list-create'),
#     path('candidates/<int:pk>/', CandidateDetailView.as_view(), name='candidate-detail'),
# ]

# from django.http import HttpResponse
# from django.urls import path

# def test_view(request):
#     return HttpResponse("Test is working!")

# urlpatterns = [
#     path('test/', test_view),
# ]

# Define your views
from django.urls import path, include
from django.contrib import admin
from django.http import HttpResponse
from .views import get_user_roles, assign_user_role, api_login_view, get_redirect_url_for_role # Import the new login view

# Define your views
def test_view(request):
    return HttpResponse("Test page is working!")

def home_view(request):
    return HttpResponse("Welcome to the Candidate Screening App!")

# Define the URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    #5-2-2025 ch5 removed home and test view
    # API URLs
    path('api/get-user-roles/', get_user_roles, name='get_user_roles'),
    path('api/assign-user-role/', assign_user_role, name='assign_user_role'),
    # path('api/login/', api_login_view, name='api_login'),  # 5-2-2025 ch3
    path('api/api-login-view/',api_login_view, name ='api_login_view')
]
