
# removes white space before after data.
# removes all spaces
def remove_whitespace(known_data):
    known_data.strip()
    known_data = known_data.replace(" ", "")
    return known_data


# intialise list to hold three sides and two angles
solved_triangle = ["a", "b", "c", "A", "B"]

# initialise given information (starts with nothing)
num_given = 0
add_one = "no"

while num_given < 2:

    # replace with checking function in due course
    get_data = input("Enter a known side / angle (eg: a = 3 or B = 35): ")
    clean_data = remove_whitespace(get_data)

    if add_one == "yes":
        num_given += 1

    angle_side = clean_data[0]
    value = clean_data[2:]

    print(f"The angle / side is: {angle_side}")
    print(f"The value is: {value}")
