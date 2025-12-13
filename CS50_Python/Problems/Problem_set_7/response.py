from validator_collection import checkers
email=input("What's your email address? ")
if False == checkers.is_email(email):
    print("Invalid")
else:
    print("Valid")
