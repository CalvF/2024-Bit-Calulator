#Generates heading (eg: ---- Heading ----)
def statement_generator(statement, decoration):
    print(f"{decoration * 5} {statement} {decoration * 5}")


# Displays instructions
def instructions():
    statement_generator ("Instruction",  "'")


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

 # Ask user fpr width and loop until they
#enter a number that is more than zero
def int_check(question,low):
    error = "Please enter a number that is more thaan zero\n"
    while True:

        try:
            #ask the user for a number
            response = int(input(question))

            # check that the number is more than zero
            if response > 0:
                return response
            else:
                print(error)


        except ValueError:
            print(error)


# calculate how many bits are needed to represent an integer
def image_calc():
    # Get the image dimension
    width = int_check( "Width ", 1)
    height = int_check( "Height", 1)

    # Calculate the number of pixels and multiply by 24 to gett the number of bits
    num_pixels = width * height
    num_bits = num_pixels * 24

    #set up answer and return it
    answer = (f"Number of pixels: {width} x {height} = {num_pixels}"
              f"\nNumber of bits: {num_pixels} x 24 = {num_bits}")

    return answer


# calculate how many bits are needed to represent an integer
def integer_calc():
    #ask the user to enter omterger( more than / equal to 0)
    integer = int_check ( "intger", 0)

    #Convert the integer to binary amd worl out the number of bits needed
    raw_binary = bin(integer)


    #remove the leading 'ob' from the raw binary conversion
    binary = raw_binary[2:]
    num_bits = len(binary)

    #set up answer and returm it
    answer = f"{integer} in binary is {binary}, we need {num_bits} to represent it."

    return answer

#calculate nimber of bits needed to represent text in ascii

def calc_text_bits():
    #get text from user
    response = input ("Enter some text: ")

    #calculate bits needed
    num_chars =len(response)
    num_bits = num_chars * 8


    # Set up answer and return it
    answer = (f"{response} has {num_chars} characters."
              f"\nWe need {num_chars} x 8 to represent it"
              f"\nwhich is {num_bits} bits")

    return answer



#main routine goes here

# Display instructions if requested
want_instructions = input("Press <enter> to read the instructions"
                          "or any key to continue " )

if want_instructions == "":
    instructions()

while True:
    file_type = get_filetype()

    if file_type == "xxx":
        break

    #if user chose 'i', ask if they want an image / interger
    if file_type == 'i':

        want_image = input("Press <enter> for an integer or any key for an image")
        if want_image == "":
            file_types = "integer"

        else:
            file_type = "image"

    if file_type == "image":
        image_ans = image_calc()
        print(image_ans)
    elif file_type == "integer":
        integer_ans = integer_calc()
        print(integer_ans)
    else:
        text_ans = calc_text_bits()
        print(text_ans)

