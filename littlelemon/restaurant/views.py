from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView ,RetrieveUpdateDestroyAPIView
from .serializers import *
from .models import Menu
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions


def index(request):
    return render(request, 'index.html', {})


class MenuItemView(ListCreateAPIView):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()


class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    def get_permissions(self):
        if self.request.method == 'PATCH' or self.request.method == 'PUT' or self.request.method == 'DELETE':
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()

class BookingViewSet(ModelViewSet):
   queryset = Booking.objects.all()
   serializer_class = BookingSerializer

   def get_permissions(self):
    if self.action == 'list':
        permission_classes = [permissions.IsAuthenticated]
    else:
        permission_classes = [permissions.IsAdminUser]
    return [permission() for permission in permission_classes]