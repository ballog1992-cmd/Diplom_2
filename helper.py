from faker import Faker

faker = Faker()


def generate_registration_data():
    
    email = faker.email()
    password = faker.password(length=6)
    name = faker.first_name()

    return name, email, password