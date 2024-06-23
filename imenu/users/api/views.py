from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.hashers import make_password

from users.models import User
from users.api.serializers import UserSerializer

class UserApiViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        request.data['password'] = make_password(request.data['password'])
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        password = request.data['password']
        
        if password:
            request.data['password'] = make_password(password)
        else:
            request.data['password'] = request.user.password

        return super().update(request, *args, **kwargs)