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
    
    @property
    def label_length(self):
        return len(self.first_name) + len(self.last_name)
    
class BusinessContact(BaseContact):
    def __init__(self, first_name, last_name, phone, email, job_title, company_name, work_phone):
        super().__init__(first_name, last_name, phone, email)
        self.job_title = job_title
        self.company_name = company_name
        self.work_phone = work_phone

    def contact(self):
        print(f'Wybieram numer {self.work_phone} i dzwonię do {self.first_name} {self.last_name} z firmy {self.company_name}')

def create_contacts(contact_type, count):
    contacts = []
    for _ in range(count):
        first_name = fake.first_name()
        last_name = fake.last_name()
        phone = fake.phone_number()
        email = fake.email()

        if contact_type == BaseContact:
            contact = BaseContact(first_name, last_name, phone, email)
        elif contact_type == BusinessContact:
            job_title = fake.job()
            company_name = fake.company()
            work_phone = fake.phone_number()
            contact = BusinessContact(first_name, last_name, phone, email, job_title, company_name, work_phone)
        contacts.append(contact)
    return contacts

