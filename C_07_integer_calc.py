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

# Main routine goes here
for item in range(0,2):
    integer = int_check( "Integer: ", 0)
    print(integer)

print()

for item in range(0,2):
    height = int_check( "width: ",1)
    print(height ) 