from rest_framework import viewsets
from django.contrib.auth.models import Group
from ..serializers import BaseGroupSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = BaseGroupSerializer
