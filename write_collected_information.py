informations = {}

while True:
    while True:
        full_name = input("Please input your full name: ")
        if not full_name.replace(" ", "").isalpha():
            print("Invalid Input! Please input letters only.")

        elif not full_name.istitle():
            print("Invalid Input! The first letter in each word should be capitalized, followed by lowercase characters.")

        elif len(full_name) <3:
            print("Invalid Input! Please provide a longer name.")

        else:
            break
    
    while True:
        age = input(f"How old are you {full_name}?: ")

        if not age.isdigit():
            print("Invalid Input! Please input numbers ranging from 0 to 150 only.")

        elif int(age) < 0 or int(age) > 150:
            print("Invalid Input! Please provide a valid number for age between 0 and 150.")

        else: 
            break

    while True:
        sex = input("Are you a Male or Female?: ")
        
        if sex in ["Male", "Female"]:
            break

        else:
            print("Invalid Input! Input 'Male' or 'Female'.")
    
    while True:
        contact_number = input("Please input your contact number: ")

        if len(contact_number) == 11:
            break
        
        else:
            print("Invalid Input! Please input an 11-digit number.")
    
    while True:
        status = input("Are you Single, Married, Widowed, or Divorced?: ")

        if status in ["Single", "Married", "Widowed", "Divorced"]:
            break

        else:
            print("Invalid Input! Input 'Single','Married','Divorced, or 'Widowed' only.")
    
    while True:
        mother_name = input("Please input your mother's name: ")
        
        if not mother_name.replace(" ", "").isalpha():
            print("Invalid Input! Please input letters only.")
        
        elif not mother_name.istitle():
            print("Invalid Input! The first letter in each word should be capitalized, followed by lowercase characters.")

        elif len(mother_name) <3:
            print("Invalid Input! Please provide a longer name.")

        else:
            break
    
    while True:
        father_name = input("Please input your father's name: ")
        
        if not father_name.replace(" ", "").isalpha():
            print("Invalid Input! Please input letters only.")
        
        elif not father_name.istitle():
            print("Invalid Input! The first letter in each word should be capitalized, followed by lowercase characters.")

        elif len(father_name) <3:
            print("Invalid Input! Please provide a longer name.")

        else:
            break

    with open("./collected_informations.txt", "a") as info:
        informations = {
            info.write(f'Name: {full_name}\n'),
            info.write(f'Age: {age}\n'),
            info.write(f'Sex: {sex}\n'),
            info.write(f'Contact Number: {contact_number}\n'),
            info.write(f'Marital Status: {status}\n'),
            info.write(f"Mother's Name: {mother_name}\n"),
            info.write(f"Father's Name: {father_name}\n")
        }

    #ask the user if they would like to input another entry
        #If the response is "no," print a message indicating that the data has been written to the file.
