#Generates heading (eg: ---- Heading ----)
def statement_generator(statement, decoration):
    print(f"{decoration * 5} {statement} {decoration * 5}")


# Displays instructions
def instructions():
    statement_generator ("Instruction",  "'")



    print(''' 
Instructions go here.
- instructions 1
- instructions 2
- etc
''')




#main routine goes here

# Display instructions if requested
want_instructions = input("Press <enter> to read the instructions"
                          "or any key to continue " )

if want_instructions == "":
    instructions()

print("program continues")
