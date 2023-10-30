from faker import Faker

fake = Faker()

class BaseContact:
    def __init__(self, first_name, last_name, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
    
    def contact(self):
        print(f"Wybieram numer {self.phone} i dzwonię do {self.first_name} {self.last_name}")
    
    
