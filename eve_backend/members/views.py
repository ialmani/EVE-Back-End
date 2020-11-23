from rest_framework.generics import CreateAPIView

from .models import Member
from .serializers import MemberSerializer


class SignUpView(CreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer