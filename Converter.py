def unit_check(question):
    valid = False
    while not valid:

        response = input("What is your chosen unit?: ")

        if response == "time" or response == "t":
            return "You Have Chosen Time"

        elif response == "distance" or response == "d":
            return "You Have Chosen Distance"

        elif response == "weight" or response == "w":
            return "You Have Chosen Weight"

        else:
            print("Please choose a valid file type in the form of an integer, text or image")
            print()


def unit_check_weight(question):
    valid = False
    while not valid:

        response = input(question)

        if response == "grams" or response == "g":
            return "Grams"

        elif response == "milligrams" or response == "mg":
            return "Milligrams"

        elif response == "Kilograms" or response == "kg":
            return "Kilograms"

        else:
            print("Please choose a valid file type in the form of an integer, text or image")
            print()

def statement_generator(text, decoration):
    # Make string with five characters
    ends = decoration * 5

    # add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


def instructions():
    statement_generator("Instructions/information", "-")
    print()
    print("Please choose a number than is greater than or equal to one and less than or equal to 200")
    print()
    print("Complete as many calculations as necessary, pressing <enter> at the end of each "
          "calculation or any key to quit.")
    print()
    statement_generator("Converter Of Time, Weight and Distance", "+")
    return ""


def distance_bits():
    print()
    to_be_converted = input("Enter the unit of distance you are converting, being Meters, Centimeters, or Kilometers: ")
    to_be_converted_to = input("Enter the unit of distance you are converting to, being Meters, Centimeters, "
                               "or Kilometers: ")

    print()
    heading = input("{} to {}".format(to_be_converted, to_be_converted_to))
    statement_generator("You have chosen {}", "+".format(heading))
    print()

    return ""


def time_bits():
    print()
    to_be_converted = input("Enter the unit of time you are converting, being Seconds, Minutes, Hours: ")
    to_be_converted_to = input("Enter the unit of time you are converting to, being Seconds, Minutes, Hours: ")

    print()
    heading = input("{} to {}".format(to_be_converted, to_be_converted_to))
    statement_generator("You have chosen {}", "+".format(heading))
    print()

    return ""


def weight_bits():
    print()
    to_be_converted = unit_check_weight(
        "Enter the unit of weight you are converting, being Milligrams, Grams, Kilograms: ")
    to_be_converted_to = unit_check_weight("Enter the unit of distance you are converting to, being Milligrams, Grams, "
                                           "Kilograms: ")

    print()
    heading = input("{} to {}".format(to_be_converted, to_be_converted_to))
    statement_generator("You have chosen {}", "+".format(heading))
    print()

    return ""


statement_generator("Converter Of Time, Weight and Distance", "+")

first_time = input("Press <enter> to see the instructions or any key to continue")
if first_time == "":
    instructions()

keep_going = ""
while keep_going == "":
    data_type = unit_check("What is your chosen unit?: ")
    print(data_type)

    if data_type == "distance":
        distance_bits()

    elif data_type == "time":
        time_bits()

    else:
        weight_bits()

    print()
    keep_going = input("Press <enter> to continue or any key to quit")

print()
print("Thanks for using the Converter Of Time, Weight and Distance")
