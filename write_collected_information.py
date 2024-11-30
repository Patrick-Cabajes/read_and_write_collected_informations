informations = {}
#open a text file

while True:
    while True:
        full_name = input("Please input your full name: ")
        if not full_name.isalpha():
            print("Invalid Input: Please input letter only")

        else:
            break

    #ask for more information following the format from the second loop

    #store the information in the array and write the collected data to the text file

    #ask the user if they would like to input another entry
        #If the response is "no," print a message indicating that the data has been written to the file.
