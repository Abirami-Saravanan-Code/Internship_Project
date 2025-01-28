from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Existing API views for user roles
@api_view(['GET'])
def get_user_roles(request):
    users = User.objects.all()
    data = [{'id': user.id, 'username': user.username, 'roles': [group.name for group in user.groups.all()]} for user in users]
    return Response(data)

@api_view(['POST'])
def assign_user_role(request):
    user_id = request.data.get('user_id')
    role = request.data.get('role')
    user = User.objects.get(id=user_id)
    group = Group.objects.get(name=role)
    user.groups.add(group)
    return Response({'message': f'Role {role} assigned to user {user.username}'})

# New API view for login with role-based redirection
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
        if user.groups.filter(name=selected_role).exists():
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
    elif role == 'hiring-manager':
        return '/hiring-manager/dashboard/'
    elif role == 'sourcing-team':
        return '/sourcing-team/dashboard/'
    elif role == 'interviewer':
        return '/interviewer/dashboard/'
    elif role == 'candidate':
        return '/candidate/dashboard/'
    return '/'
