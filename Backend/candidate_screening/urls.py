"""
URL configuration for candidate_screening project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin 
#from django.urls import path  # 5-2-25 ch1
# from .views import get_user_roles, assign_user_role, api_login_view  # check a

# urlpatterns = [
#     path('admin/', admin.site.urls),  # Admin URL
#     path('api/get-user-roles/', get_user_roles, name='get_user_roles'),
#     path('api/assign-user-role/', assign_user_role, name='assign_user_role'),
#     path('api/login/', api_login_view, name='api_login_view'),
#     # Other API paths...
# ]

from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('recruit_right.urls')),  # Includes recruit_right URLs
]

