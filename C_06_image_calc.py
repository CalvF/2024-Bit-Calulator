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

# Main routine goes here
for item in range(0,2):
    integer = int_check( "Integer: ", 0)
    print(integer)

print()

for item in range(0,2):
    height = int_check( "width: ",1)
    print(height ) 