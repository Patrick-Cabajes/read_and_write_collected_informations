informations = {}

while True:
    while True:
        full_name = input("Please input your full name: ")
        if not full_name.replace(" ", "").isalpha():
            print("Invalid Input: Please input letters only!")

        elif not full_name.istitle():
            print("Invalid Input: The first letter in each word should be capitalized, followed by lowercase characters!")

        elif len(full_name) <3:
            print("Invalid Input: Please provide a longer name!")

        else:
            break
    
    while True:
        age = input(f"Please input the age of {full_name}: ")

        if not age.isdigit():
            print("Invalid Input: Please input numbers only")

        elif int(age) < 0 or int(age) > 150:
            print("Invalid Input: Please provide a valid number for age between 0 and 150")

        else: 
            break

    with open("./collected_informations.txt", "a") as info:
        informations = {
            info.write(f'Name: {full_name}\n'),
            info.write(f'Age: {age}\n')
        }

    #ask the user if they would like to input another entry
        #If the response is "no," print a message indicating that the data has been written to the file.
