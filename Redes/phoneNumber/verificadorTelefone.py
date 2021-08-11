import phonenumbers

from phonenumbers import geocoder

phone = input('Digite o telefone no formato +55DDNUMERO:')

phone_number = phonenumbers.parse(phone)

g = geocoder.description_for_number(phone_number, 'pt')

print(g)

