import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','user_project.settings')

import django
django.setup()

### FAKE POP SCRIPT

from faker import Faker

from user_app.models import userProfile


#fake = Faker()
fakegen = Faker()
for x in range(5):
    fake_fname = fakegen.first_name()
    fake_lname = fakegen.last_name()
    fake_email = fakegen.email()
    userProfile.objects.get_or_create(first_name=fake_fname, last_name=fake_lname, email=fake_email)


"""
class UserTestCaseMixin:
    def _create_user(self, email=None, first_name=None):
        return userProfile.objects.create(
          email=email,
          first_name=first_name
          
         
        )
        """

