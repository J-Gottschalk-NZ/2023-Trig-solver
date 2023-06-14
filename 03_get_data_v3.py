# removes white space before after data.
# removes all spaces
def remove_whitespace(known_data):
    known_data.strip()
    known_data = known_data.replace(" ", "")
    return known_data


# get angle and side
def get_angle_side():
    valid_side_ang = ["a", "b", "c", "A", "B"]

    while True:
        # replace with checking function in due course
        get_data = input("Enter a known side / angle (eg: a = 3 or B = 35): ")
        clean_data = remove_whitespace(get_data)

        angle_side = clean_data[0]

        value = clean_data[2:]

        # Check numerical values are valid
        if angle_side in valid_side_ang[:3]:
            # sides need to be more than zero (default)
            value = num_check(value)

        else:
            # angles need to be more than zero AND less than 90
            value = num_check(value, 90)

        if value != "invalid":
            return [angle_side, value]
        else:
            print("Please enter a valid number (more than 0, less than 90 for an angle)")


def num_check(amount, high=None):

    try:
        amount = float(amount)
        if amount <= 0:
            return "invalid"
        elif high is not None and amount >= high:
            return "invalid"
        else:
            return amount

    except ValueError:
        return "invalid"


# intialise list to hold three sides and two angles
solved_triangle = ["a", "b", "c", "A", "B"]

# initialise given information (starts with nothing)
num_given = 0
add_one = "no"

thing = get_angle_side()
print(thing)
