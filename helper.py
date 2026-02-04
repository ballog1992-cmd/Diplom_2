from faker import Faker
import random
faker = Faker()


def generate_registration_data():
    
    email = f"{random.randint(1, 999)}{faker.free_email()}"
    password = faker.password(length=6)
    name = faker.first_name()

    return name, email, password