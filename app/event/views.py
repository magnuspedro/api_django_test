from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Event

from event import serializers


class EventViewSet(viewsets.ModelViewSet):
    """Manage Event in the database"""
    serializer_class = serializers.EventSerializer
    queryset = Event.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Retrive the event for the authenticated user"""
        return self.queryset.all()

    def get_serializer_class(self):
        """Retrun appropriated serializer class"""
        if self.action == 'list':
            return serializers.EventDetailSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new event"""
        serializer.save()
