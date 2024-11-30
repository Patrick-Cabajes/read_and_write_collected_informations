while True:
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
            content = file.read()

            personal_informations = content.split("=" * 40)
            found = False   

            for person in personal_informations:
                if (f"Name: {name_search}") in person:
                    found = True
                    print(f"\nInformation found for {name_search}:") 
                    print("=" * 40)
                    print(person.strip())
                    print("=" * 40)
               
            if not found:
                print(f"No information is found for {name_search}. Please check the name and try again.")
    
        while True:
            search_again = input("Would you like to search for another person? Please input 'yes' or 'no': ")
            if search_again in ["yes", "no"]:
                break 
        break

    if search_again == "yes":
        print("Request Accepted!")

    elif search_again == "no":
        print("Thank you for using the search program!")
        break

    else:
        print("Invalid Input! Please input 'yes' or 'no' only.")