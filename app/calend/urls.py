from django.urls import path, include
from rest_framework.routers import DefaultRouter

from calend import views

router = DefaultRouter()
router.register('', views.CalendarViewSet)

app_name = 'calendar'

urlpatterns = [
    path('', include(router.urls))
]
