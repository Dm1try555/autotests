import random

from data.data import Person
from faker import Faker

faker_ru = Faker('ru_RU')
Faker.seed()

def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        firstname= faker_ru.first_name(),
        lastname = faker_ru.last_name(),
        age= random.randint(10,80),
        department=faker_ru.job(),
        salary= random.randint(1000,99999),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        id_meeting=random.randint(1000, 9999),
        ipn_of_the_participant=random.randint(1000000000000, 2000000000000),
        name_of_the_company=faker_ru.company()
    )

def generated_file():
    path = rf'C:\Users\Dima\Downloads\Telegram Desktop\filetest{random.randint(0,999)}.txt'
    file = open(path, 'w+')
    file.write(f'Hello World{random.randint(0,999)}')
    file.close()
    return file.name, path
