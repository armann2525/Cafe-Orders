import pytest
from orders.models import Order

@pytest.mark.django_db
def test_order_creation():
    order = Order.objects.create(
        table_number=5,
        items='Pizza, Cola',
        total_price=20.5,
        status='new'
    )
    assert order.table_number == 5
    assert order.items == 'Pizza, Cola'
    assert order.total_price == 20.5
    assert order.status == 'new'

@pytest.mark.django_db
def test_order_status_choices():
    order = Order.objects.create(
        table_number=3,
        items='Burger, Fries',
        total_price=15.0,
        status='paid'
    )
    assert order.get_status_display() == 'Paid'
