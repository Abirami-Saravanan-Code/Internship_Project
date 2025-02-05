from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.contrib.auth.models import User, Group
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

@csrf_exempt
@api_view(['POST'])
def api_login_view(request):
    data = request.data

    email = data.get('email')
    password = data.get('password')
    selected_role = data.get('selectedRole')
    
    try:
        # Find the user by email (assuming email is used as username)
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return JsonResponse({'error': 'Invalid email or password'}, status=400)
    
    # Authenticate using email and password
    user = authenticate(request, username=user.username, password=password)
    
    if user is not None:
        login(request, user)  # Log the user in

        # Check if the user is in the selected role group
        if user.groups.filter(name=selected_role).exists():  # This line is important!
            return JsonResponse({
                'message': 'Login successful',
                'role': selected_role,
                'redirect_url': get_redirect_url_for_role(selected_role)
            })
        else:
            return JsonResponse({'error': 'You do not have access to this role'}, status=403)
    else:
        return JsonResponse({'error': 'Invalid email or password'}, status=400)

def get_redirect_url_for_role(role):
    """Returns the redirect URL based on the user's role"""
    if role == 'admin':
        return '/admin/dashboard/'
    elif role == 'Hiring Manager':  # Updated to match the role with spaces and capitalization
        return '/hiring-manager/dashboard/'
    elif role == 'sourcing-team':
        return '/sourcing-team/dashboard/'
    elif role == 'interviewer':
        return '/interviewer/dashboard/'
    elif role == 'candidate':
        return '/candidate/dashboard/'
    return '/'  # Default fallback if no match

# Added function to fetch user roles
@csrf_exempt
@api_view(['GET'])
def get_user_roles(request):
    """Returns a list of available roles in the system"""
    roles = ['admin', 'Hiring Manager', 'sourcing-team', 'interviewer', 'candidate']  # Example roles
    return JsonResponse({'roles': roles})

@csrf_exempt
@api_view(['POST'])
def assign_user_role(request):
    """Assign a role to a user"""
    data = request.data
    email = data.get('email')
    role = data.get('role')
    
    try:
        user = User.objects.get(email=email)
        group, created = Group.objects.get_or_create(name=role)  # Ensure matching role name
        user.groups.add(group)
        return JsonResponse({'message': f'Role {role} assigned to {email}'})
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

# Protecting views for "Hiring Manager"
@csrf_exempt
@api_view(['GET'])
def hiring_manager_dashboard(request):
    """Only accessible by users with 'Hiring Manager' role"""
    if not request.user.groups.filter(name='Hiring Manager').exists():  # Updated group name
        return JsonResponse({'error': 'You do not have access to this dashboard'}, status=403)
    return JsonResponse({'message': 'Welcome to the Hiring Manager Dashboard'})
