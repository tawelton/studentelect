from django.test import TestCase
from account import models as amod
from django.contrib.auth import models as pmod
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime

class AccountTests(TestCase):
    fixtures = ['account.yaml']

    def setUp(self):

        self.homer = amod.User()
        self.homer.username = "homer2"
        self.homer.set_password('doh!')
        self.homer.first_name = "Homer"
        self.homer.last_name = "Simpson"
        self.homer.birthdate = datetime(2000,1,1)

        # add permissions

        self.homer.save()

    def test_user_get(self):
        u1 = amod.User.objects.get(id=1)
        self.assertEqual(u1.first_name, 'Tanner', msg="Name should have been Tanner")

    def test_user_create(self):
        u = amod.User()
        u.username = 'hp'
        u.first_name = 'Harry'
        u.last_name = 'Potter'
        u.set_password('wizard')
        u.email = 'harry@potter.com'
        u.birthdate = datetime(2000,1,1)
        u.save()
        u2 = amod.User.objects.get(id=u.id)
        self.assertEqual(u.first_name, u2.first_name, msg="User not created")

    def test_user_login(self):
        credentials = {
            'username': 'homer2',
            'password': 'doh!',
        }

        response = self.client.post('/account/login/', credentials)

        request = response.wsgi_request

        self.assertTrue(request.user.is_authenticated, msg='User should have authenticated')
        self.assertEqual(request.user.id, self.homer.id, msg='User should have been homer')
        self.assertEqual(response.status_code, 302, msg='User wasn\'t redirected')

    def test_user_logout(self):

        response = self.client.get('/account/logout/')

        request = response.wsgi_request

        self.assertFalse(request.user.is_authenticated, msg="User shouldn't be authenticated")
        self.assertEqual(response.status_code, 302, msg='User wasn\'t redirected')

    def test_group_permissions(self):

        perm = pmod.Permission()

        perm.codename = 'firstpermission'
        perm.name = 'First Permission Test'
        perm.content_type = pmod.Permission.objects.get(codename='add_user').content_type
        perm.save()

        self.assertTrue(pmod.Permission.objects.filter(codename='firstpermission').exists(), msg="Permission - 'firstpermission' - should have been created")

        group = pmod.Group()

        group.name = "First Group"
        group.save()
        
        self.assertTrue(pmod.Group.objects.filter(name='First Group').exists(), msg="Group = 'First Group' - should have been created")

        group.permissions.add(pmod.Permission.objects.get(codename='firstpermission'))
        group.save()

        self.assertTrue(pmod.Group.objects.get(name='First Group').permissions.filter(codename="firstpermission").exists(), msg="Group - 'First Group' - should have the permission 'firstpermission'")

    def test_users_and_groups(self):
        group = pmod.Group()

        group.name = "First Group"
        group.save()
        
        self.assertTrue(pmod.Group.objects.filter(name='First Group').exists(), msg="Group = 'First Group' - should have been created")

        self.homer.groups.add(pmod.Group.objects.get(name='First Group'))

        self.homer.save()

        self.assertTrue(amod.User.objects.get(username=self.homer.username).groups.filter(name="First Group").exists(), msg="Homer should be a part of group 'First Group'")

    def test_change_password(self):
        self.homer.set_password('reset')
        self.homer.save()

        self.assertFalse(authenticate(username="homer2", password="reset") is None, msg="User - 'homer2' - should have authenticated with password 'reset'")