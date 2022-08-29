import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

phone_number1 = phonenumbers.parse("+2349087445111")
phone_number2 = phonenumbers.parse("+23230088788")
phone_number3 = phonenumbers.parse("+447527487660")

print(phone_number1)

print(geocoder.description_for_number(phone_number1,'en'), carrier.name_for_number(phone_number1,'en'))
print(geocoder.description_for_number(phone_number2,'en'), carrier.name_for_number(phone_number2,'en'))
print(geocoder.description_for_number(phone_number3,'en'), carrier.name_for_number(phone_number3,'en'))
