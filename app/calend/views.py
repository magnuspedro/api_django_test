from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Calendar

from calend import serializers


class CalendarViewSet(viewsets.ModelViewSet):
    """Manage calendar in the database"""
    serializer_class = serializers.CalendarSerializer
    queryset = Calendar.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Retrive the calendar for the authenticated user"""
        return self.queryset.all()

    def get_serializer_class(self):
        """Retrun appropriated serializer class"""
        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new event"""
        serializer.save()
