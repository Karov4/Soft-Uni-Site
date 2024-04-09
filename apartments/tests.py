from django.contrib.auth.models import Group
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Apartment, Rent, Review, Favorite

class ApartmentModelTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_apartment_creation(self):
        apartment = Apartment.objects.create(name='Test Apartment', description='This is a test apartment', price=100.00, available=True, owner=self.user, location='Test Location', image_url='http://test.com')
        self.assertEqual(apartment.name, 'Test Apartment')

class RentModelTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.apartment = Apartment.objects.create(name='Test Apartment', description='This is a test apartment', price=100.00, available=True, owner=self.user, location='Test Location', image_url='http://test.com')

    def test_rent_creation(self):
        rent = Rent.objects.create(tenant=self.user, apartment=self.apartment, start_date='2022-01-01', end_date='2022-12-31')
        self.assertEqual(rent.tenant.username, 'testuser')

class ReviewModelTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.apartment = Apartment.objects.create(name='Test Apartment', description='This is a test apartment', price=100.00, available=True, owner=self.user, location='Test Location', image_url='http://test.com')
        self.rent = Rent.objects.create(tenant=self.user, apartment=self.apartment, start_date='2022-01-01', end_date='2022-12-31')

    def test_review_creation(self):
        review = Review.objects.create(rating=5, comment='Great!', lease=self.rent, date='2022-01-01')
        self.assertEqual(review.rating, 5)

class FavoriteModelTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.apartment = Apartment.objects.create(name='Test Apartment', description='This is a test apartment', price=100.00, available=True, owner=self.user, location='Test Location', image_url='http://test.com')

    def test_favorite_creation(self):
        favorite = Favorite.objects.create(apartment=self.apartment, user=self.user)
        self.assertEqual(favorite.user.username, 'testuser')

class CustomUserModelTest(TestCase):
    def setUp(self):
        # Create the 'Renters' group before running the test
        Group.objects.create(name='Renters')

    def test_custom_user_creation(self):
        User = get_user_model()
        user = User.objects.create_user(username='testuser', password='12345', user_type='renter')
        self.assertEqual(user.user_type, 'renter')


class ApartmentViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='12345')

        # Get or create the 'Leasers' group
        leasers_group, created = Group.objects.get_or_create(name='Leasers')
        self.user.groups.add(leasers_group)

        self.client.login(username='testuser', password='12345')

        self.apartment = Apartment.objects.create(name='Test Apartment', description='This is a test apartment',
                                                  price=100.00, available=True, owner=self.user,
                                                  location='Test Location', image_url='http://test.com')
    def test_add_apartment_view(self):
        response = self.client.get(reverse('add_apartment'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'apartments/apartment_add.html')

    def test_my_apartments_view(self):
        response = self.client.get(reverse('my_apartments'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'apartments/my_apartments.html')
        self.assertTrue('apartments' in response.context)
        self.assertTrue(self.apartment in response.context['apartments'])

    def test_edit_apartment_view(self):
        response = self.client.get(reverse('edit_apartment', args=[str(self.apartment.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'apartments/edit_apartment.html')

    def test_delete_apartment_view_get(self):
        response = self.client.get(reverse('delete_apartment', args=[str(self.apartment.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'apartments/confirm_delete.html')

    def test_delete_apartment_view_post(self):
        response = self.client.post(reverse('delete_apartment', args=[str(self.apartment.id)]))
        self.assertEqual(response.status_code, 302)  # Redirects to 'my_apartments'
        self.assertFalse(Apartment.objects.filter(id=self.apartment.id).exists())
