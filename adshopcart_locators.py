from faker import Faker

fake = Faker(locale='en_CA')

adShopCart_url = 'https://advantageonlineshopping.com/#/'
create_user_url = 'https://advantageonlineshopping.com/#/register'
username = fake.user_name()
password = fake.password()
email = fake.email()
first_name = fake.first_name()
last_name = fake.last_name()
full_name = f'{first_name} {last_name}'
phone_number = fake.phone_number()
country = fake.country()
city = fake.city()
address = fake.street_address()
province = fake.province_abbr()
postalcode = fake.postalcode
subject = 'I have great experience using the AOS Cart'

