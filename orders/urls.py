from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from .api import OrderViewSet

router = DefaultRouter()
router.register(r'api/orders', OrderViewSet)

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('create/', views.order_create, name='order_create'),
    path('<int:pk>/update/', views.order_update, name='order_update'),
    path('<int:pk>/delete/', views.order_delete, name='order_delete'),
]

urlpatterns += router.urls
