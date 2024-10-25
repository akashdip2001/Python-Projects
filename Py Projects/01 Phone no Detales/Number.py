# pip install phonenumbers 

import phonenumbers
from phonenumbers import timezone,geocoder,carrier

number=input("Enter the phone number with country code: ")

phone_number=phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone_number)
car=carrier.name_for_number(phone_number,"en")
reg=geocoder.description_for_number(phone_number,"en")

print(phone_number)
print("Timezone: ",time)
print("Carrier: ",car)
print("Region: ",reg)


# # Additional information that can be retrieved using the phonenumbers library
# is_valid = phonenumbers.is_valid_number(phone_number)
# is_possible = phonenumbers.is_possible_number(phone_number)
# region_code = phonenumbers.region_code_for_number(phone_number)

# print("Is valid number: ", is_valid)
# print("Is possible number: ", is_possible)
# print("Region code: ", region_code)
# # Note: Finding the owner's name of a phone number is not possible with the phonenumbers library
# # Checking if the number is a possible number for a given region
# region = "US"  # You can change this to any region code you want to check against
# is_possible_for_region = phonenumbers.is_possible_number_for_type(phone_number, phonenumbers.PhoneNumberType.MOBILE)

# # Getting the type of the number (e.g., mobile, fixed-line, etc.)
# number_type = phonenumbers.number_type(phone_number)

# print("Is possible number for region (US): ", is_possible_for_region)
# print("Number type: ", number_type)
# # and generally requires access to a private database or service, which may not be legal or ethical.
# # Checking if the number is a valid mobile number
# is_mobile = phonenumbers.number_type(phone_number) == phonenumbers.PhoneNumberType.MOBILE

# # Checking if the number is a valid fixed-line number
# is_fixed_line = phonenumbers.number_type(phone_number) == phonenumbers.PhoneNumberType.FIXED_LINE

# print("Is mobile number: ", is_mobile)
# print("Is fixed-line number: ", is_fixed_line)
# # Therefore, it is not recommended to attempt this without proper authorization.

# #print("Owner name lookup is not supported with the current library.")