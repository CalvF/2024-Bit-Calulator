# ask user for the file type (interger / image / text / xxx)

def get_filetype():

    while True:
        response = input("File type: ").lower()

        # Check for 'i' or the exit code
        if response == "xxx" or response == "i":
            return response


        # check if it's an integer
        elif response in ['integer', 'int']:
            return "integer"

        #Check for an image...
        elif response in ['image', 'picture', 'img', 'p']:
            return "image"

        #check for text...
        elif response in {"text", 'txt', 't'}:
            return "text"

        # IF the response is invalid output an error
        else:
            print("Please enter a valid file type")


#main routine goes here
while True:
    file_type = get_filetype()

    #if user chose 'i', ask if they want an image / interger
    if file_type == 'i':

        want_image = input("Press <enter> for an integer or any key for an image")
        if want_image == "":
            file_types = "integer"

        else:
            file_type = "image"

    print(f"You chose {file_type}")

    if file_type== "xxx":
         break