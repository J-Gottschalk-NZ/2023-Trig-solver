
# intialise variables, lists and dictionaries
problem_num = 0


# Ask user for sides / angles and display unknown sides angles
while True:
    problem_num += 1

    print()
    print(f"Problem {problem_num}")
    get_data = input("Enter the known sides / angles: ")

    if get_data == "xxx":
        break

# Output problem summary and write to file
print("Thank you for using the trig solver")
