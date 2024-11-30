informations = {}
with open("./collected_informations.txt", "a") as info:

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

    #ask for more information following the format from the second loop

        informations = {
            info.write(f'Name: {full_name}\n'),
        }

    #ask the user if they would like to input another entry
        #If the response is "no," print a message indicating that the data has been written to the file.
