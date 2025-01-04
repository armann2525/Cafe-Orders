import pytest
from django.urls import reverse
from rest_framework import status
from orders.models import Order

@pytest.mark.django_db
def test_order_list_view(client):
    order = Order.objects.create(
        table_number=3,
        items='Pasta, Wine',
        total_price=30.0,
        status='new'
    )
    url = reverse('order_list')
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert 'Pasta' in response.content.decode()

@pytest.mark.django_db
def test_order_create_view(client):
    url = reverse('order_create')
    data = {
        'table_number': 4,
        'items': 'Sushi, Tea',
        'total_price': 25.0,
        'status': 'new'
    }
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['table_number'] == 4
