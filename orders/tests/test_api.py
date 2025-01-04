import pytest
from rest_framework import status
from django.urls import reverse
from orders.models import Order

@pytest.mark.django_db
def test_order_create_api(client):
    url = reverse('order-list')
    data = {
        'table_number': 6,
        'items': 'Burger, Fries',
        'total_price': 18.0,
        'status': 'new'
    }
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['table_number'] == 6

@pytest.mark.django_db
def test_order_list_api(client):
    url = reverse('order-list')
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.data, list)
    assert len(response.data) > 0
