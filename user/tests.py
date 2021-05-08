from django.test import TestCase

from user.models import Customer


class UserModelTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        # создаем модель пользователя которую будем использовать для тестов

        Customer.objects.create(
            name = 'Аlex',
            email = 'alex@mail.com',
            phone = '+380688345673',
            website = 'python.org',
            country = 'Ukraine',
            city = 'Kyiv',
        )

    def test_first_name_label(self):
        user = Customer.objects.get(pk=1)
        username = user._meta.get_field('email').verbose_name
        self.assertEquals(username, 'email')

    def test_phone_label(self):
        user = Customer.objects.get(pk=1)
        user_phone = user._meta.get_field('phone').verbose_name
        self.assertEquals(user_phone, 'телефон')

    def test_website_label(self):
        user = Customer.objects.get(pk=1)
        user_website = user._meta.get_field('website').verbose_name
        self.assertEquals(user_website, 'сайт')

    def test_country_label(self):
        user = Customer.objects.get(pk=1)
        user_country = user._meta.get_field('country').verbose_name
        self.assertEquals(user_country, 'страна')

    def test_city_label(self):
        user = Customer.objects.get(pk=1)
        user_city = user._meta.get_field('city').verbose_name
        self.assertEquals(user_city, 'город')
