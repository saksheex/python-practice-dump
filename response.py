import validators

user_email = input("What's your email address: ")
if validators.email(user_email):
    print("Valid")
else:
    print("Invalid")
