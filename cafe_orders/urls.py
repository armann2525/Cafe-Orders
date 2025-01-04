from django.contrib import admin
from django.urls import path, include
from orders import views

urlpatterns = [
    path('', views.order_list, name='order_list'),  # Главная страница
    path('admin/', admin.site.urls),
    path('orders/', include('orders.urls')),  # Маршруты для заказов
]
