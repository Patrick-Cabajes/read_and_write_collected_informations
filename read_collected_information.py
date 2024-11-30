while True:
    name_search = input("Please input the full name of the person you want to search for: ")

    if not name_search.replace(" ", "").isalpha():
        print("Invalid Input! Please input letters only.")

    elif not name_search.istitle():
        print("Invalid Input! The first letter in each word should be capitalized, followed by lowercase characters.")

    elif len(name_search) <3:
        print("Invalid Input! Please provide a longer name.")

    else:
        break
#open the text file created from the previous program and read its contents

    #using for loop, display informations about the person the user searched for
    #if the name was not found:    
        #print that the person the user was looking for was not found