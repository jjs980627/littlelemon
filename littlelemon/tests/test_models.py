from django.test import TestCase
from restaurant.models import Menu


class MenuTest(TestCase):
    def test_create_menu(self):
        menu = Menu.objects.create(Title="Pasta", Price=15.50, Inventory=20)

        self.assertEqual(str(menu), "Pasta : $15.5")
