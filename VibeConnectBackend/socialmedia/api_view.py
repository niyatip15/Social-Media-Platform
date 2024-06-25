from django.http import JsonResponse
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated
from .forms import RegisterForm

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def register(request):
    data = request.data
    message = 'success'
    form = RegisterForm({
        'email': data.get('email'),
        'name': data.get('name'),
        'password1': data.get('password1'),
        'password2': data.get('password2')
    })
    if form.is_valid():
        form.save()
    else:
        message = 'error'
    return JsonResponse({'message':message})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_profile(request):
    user = request.user
    profile_data = {
        'id': user.id,
        'name': user.name, 
        'email': user.email,
    }
    return JsonResponse(profile_data)