import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','pdrestapi.settings')
import django
django.setup()


from testapp.models import Employee
from faker import Faker
from random import *
faker=Faker()
def populate(n):
    for i in range(n):
        ename=faker.name()
        eaddr=faker.city()
        esal=choice([50000,60000,1000,55000,43000,25000])
        eno=randint(1000000000,9999999999)
        emp_record=Employee.objects.get_or_create(ename=ename,eaddr=eaddr,esal=esal,eno=eno)

populate(10)
