from django.urls import path, include
from .views import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'tables', BookingViewSet, basename='tables')

urlpatterns = [
    path('', index, name='home'),
    path('menu', MenuItemView.as_view(), name='menu'),
    path('menu/<int:pk>', SingleMenuItemView.as_view(), name='menu_single'),
    path('booking/', include(router.urls))
]
