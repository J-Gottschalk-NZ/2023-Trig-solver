# yes / no checker (simple)
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "y" or response == "yes":
            return "yes"
        elif response == "n" or response == "no":
            return "no"
        else:
            print("Please enter yes / no")


# displays instructions
def instructions():
    print('''

==== Instructions ====

This program solves a right angle triangle where 
the short sides are called 'a' and 'b' and the hypotenuse is 'c'.

The angle opposite side 'a' is called 'A' and the angle opposite 
side 'b' is called B.  

You should have at least one side and then either 
a second side or an angle (that is less than 90 degrees)

- Enter the value of your side (eg: a = 3)
- Enter the value of the second side or a known angle (eg: B = 32)

The program will solve the triangle.  

You can run the program multiple times.  Type 'xxx' at any stage to quit.
    
    ''')


# Main routine goes here

# Display instructions on request
see_instructions = yes_no("Do you want to read the instructions? ")
if see_instructions == "yes":
    instructions()

print("Program continues")
