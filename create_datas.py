from faker import Faker
import django

f = Faker(locale='zh_CN')
print(f.numerify())
print(django.get_version())
