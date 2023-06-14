import re


# removes white space before after data.
# removes all spaces
def remove_whitespace(known_data):
    known_data.strip()
    known_data = known_data.replace(" ", "")
    return known_data


# checks input matches pattern a=3
# (ie: valid letter, =, number)
def check_pattern(to_check):
    pattern = r'^[a-cA-C]=(?:\d+(?:\.\d*)?|\.\d+)$'

    if re.match(pattern, to_check):
        return "valid pattern"
    else:
        return "invalid pattern"


# checks number is more than 0
# and less than 90 if it's an angle
def num_check(amount, low=0, high=None):
    try:
        amount = float(amount)
        if amount <= low:
            return "invalid"
        elif high is not None and amount >= high:
            return "invalid"
        else:
            return amount

    except ValueError:
        return "invalid"


# get angle and side
def get_angle_side():
    valid_side_ang = ["a", "b", "c", "A", "B"]

    while True:
        # replace with checking function in due course
        get_data = input("Enter a known side / angle (eg: a = 3 or B = 35): ")
        clean_data = remove_whitespace(get_data)

        input_check = check_pattern(clean_data)
        if input_check == "invalid pattern":
            print("Please enter the data in the form a = 4 (ie: letter = number)")
            print()
            continue

        angle_side = clean_data[0]
        value = clean_data[2:]

        # Check numerical values are valid
        if angle_side in valid_side_ang[:3]:
            # sides need to be more than zero (default)
            value = num_check(value)

        else:
            # angles need to be more than zero AND less than 90
            value = num_check(value, high=90)

        if value != "invalid":
            return [angle_side, value]
        else:
            print("Please enter a valid number (more than 0, less than 90 for an angle)")


def get_given():
    # intialise list to hold three sides and two angles
    # use indices list to identify index (in case user tries to overwrite value
    solved_indices = ["a", "b", "c", "A", "B"]
    given_values = ["a", "b", "c", "A", "B"]
    need_side = ""

    # Get at least 1 side and one angle
    while True:
        # print()
        given = get_angle_side()

        if need_side is True and given[0] in ["A", "B"]:
            print("Oops - you have already given an angle, we need a side")
            continue

        # warn user that they have over-written a value if necessary
        if given[0] not in given_values:
            print(f"You have overwritten the value for {given[0]}")

        # replace the side / angle in solved triangle with its value
        index = solved_indices.index(given[0])

        given_values[index] = given[1]

        # check we have at least one side
        has_side = any(isinstance(item, (int, float)) for item in given_values[:3])

        # if we don't have a side, make sure the next input is a side
        if has_side is False:
            need_side = True

        # Check if there are at least two numbers in the full list
        number_count = sum(isinstance(item, (int, float)) for item in given_values)

        if has_side and number_count >= 2:
            return given_values


again = ""
while again == "":
    to_solve = get_given()
    print(to_solve)
    print()
    again = input("Again? Press <enter> or any key to quit ")
    print()
