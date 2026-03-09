from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from .models import CustomUser
from .serializers import SingUpSerializers

class SignUpView(CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = SingUpSerializers
    queryset = CustomUser
