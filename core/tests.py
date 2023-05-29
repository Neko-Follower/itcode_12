from django.test import TestCase, Client
from django.urls import reverse
from core import factories


# Create your tests here.
class UserTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = factories.User()
        self.group = factories.Group()
        self.course = factories.Course.create(name='ИВТ-999')

    def test_user_data(self):
        response = self.client.get(reverse('core:users'))
        self.assertEquals(response.status_code, 200)

    def test_user_detail(self):
        response = self.client.get(reverse('core:user_detail', kwargs={'pk': self.user.pk}, ))
        self.assertEquals(response.status_code, 200)

    def test_user_create(self):
        data = {
            'name': 'test_name',
            'course': self.course,
            'group': self.group,
        }
        response = self.client.post(path=reverse('core:user_create'), data=data, follow=True, )
        self.assertEquals(response.status_code, 200)
