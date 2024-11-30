while True:
    while True:
        name_search = input("Please input the full name of the person you want to search for: ")

        if not name_search.replace(" ", "").isalpha():
            print("Invalid Input! The information stored for name contains letters only.")

        elif not name_search.istitle():
            print("Invalid Input! The first letter in each word of the stored information for name is capitalized, followed by lowercase characters.")

        else:
            break

    with open("collected_informations.txt", "r") as file:
        lines = file.readlines()

        for line in lines:
            print(line.strip())
        

            
#open the text file created from the previous program and read its contents

    #using for loop, display informations about the person the user searched for
    #if the name was not found:    
        #print that the person the user was looking for was not found