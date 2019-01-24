from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Group

from group import serializers


class GroupViewSet(viewsets.ModelViewSet):
    """Manage grup in the database"""
    serializer_class = serializers.GroupSerializer
    queryset = Group.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Retrive the event for the authenticated user"""
        return self.queryset.all()

    def get_serializer_class(self):
        """Retrun appropriated serializer class"""
        if self.action == 'list':
            return serializers.GroupDetailSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new event"""
        serializer.save()
