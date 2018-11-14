import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'geodj.settings')

import django
django.setup()

# FAKE POP SCRIPT
import random
from geo_app.models import Address
from faker import Faker

fakegen = Faker()

def add_address(N=15):

    for i in range(N):
        fake_address = fakegen.address()
        fake_latitude = fakegen.latitude()
        fake_longitude = fakegen.longitude()

        adr, created = Address.objects.get_or_create(address = fake_address)
        adr.iteration = "001"
        adr.latitude = fake_latitude
        adr.longitude = fake_longitude
        adr.save()


if __name__ == '__main__':
    print("start working")
    add_address(15)
    print("done!")
