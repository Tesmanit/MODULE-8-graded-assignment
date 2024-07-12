from django.test import TestCase
from restaurant.models import Menu


class MenuTest(TestCase):
    def test_menu(self):
        instance = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(instance), "IceCream : 80")
