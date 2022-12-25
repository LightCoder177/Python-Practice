#data collecting program. 

print("Welcome to our wonderful program. Please complete the following details to proceed: ")

Data = dict()

#loop 

while True: 
    Data['info'] = dict(Name=input("Type your name here: "), Gender=input("Type your gender here: "), Occupation=input("Type your occupation here: "), Address=input("Please type your address here: "))
    print()
    print("Please confirm if the below details are correct or not.")
    for Name, info in Data['info'].items():
        print("{0:s}: {1:s}".format(Name, info))
    
    
    while True:
        yes_or_no = input("You can type yes or no to confirm: ")
        print()
        if yes_or_no.lower() == 'yes':
            print("Thank you for the verification. Please proceed to the next step.")
            break
        elif yes_or_no.lower() == 'no':
            print("Please re-enter details: ")
            print()
            break
        else:
            print("That's not the correct answer. Please re-enter your answer: ")
    if yes_or_no == "yes":
        break
