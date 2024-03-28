contact = {
    "fullname": "Jane Doe",
    "phone": "321-321-4321",
    "email": "test@test.com"
}

# Your code here
print(contact.keys())
print(contact.values())
print(contact.items())

for key in contact.keys():
    print(f"{key}: {contact[key]}")