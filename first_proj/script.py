import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_proj.settings')

import django
django.setup()

import random
from sec_app.models import User

from faker import Faker
fakegen=Faker()

def populate(N=5):
    for i in range(N):
        fake_fn=fakegen.first_name()
        fake_ln=fakegen.last_name()
        fake_email=fakegen.email()
        u=User.objects.get_or_create(first_name=fake_fn,last_name=fake_ln,email=fake_email)[0]

if __name__=='__main__':
    print("populating script")
    populate(20)
    print("populating complete!")


