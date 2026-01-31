from faker import Faker

fake = Faker()
class Generator:
    @staticmethod
    def email_generator():
        return fake.email()

    @staticmethod
    def password_generator():
        return fake.random_number(6)

    @staticmethod
    def name_generator():
        return fake.name()
