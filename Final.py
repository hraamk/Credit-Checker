"""Coursework - Software Development 1 (PRO) - Hariraam Kethisvarasuthan - 20231072 / W2051820
This code includes Part (1A,1B,1C,1D), Part 2 and Part 3"""

from graphics import *


def get_input(prompt):  # Part 1B - Credit Validation
    try:
        credit = int(input("Please enter your credits at " + prompt + " : "))
        if credit in [0, 20, 40, 60, 80, 100, 120]:  # Checking range
            return credit
        else:
            print("Out of Range")
            return True

    except ValueError:  # Checking variable type
        print("Integer Required")
        return True


def check_grade(pass_cr, defer_cr):  # Producing Outcomes

    global progress_count
    global trailer_count
    global retriever_count
    global exclude_count

    if pass_cr == 120:  # c1
        progress_count += 1
        return "Progress"

    elif pass_cr == 100:  # c2
        trailer_count += 1
        return "Progress (module trailer)"

    elif pass_cr + defer_cr <= 40:  # c5 c7 c9
        exclude_count += 1
        return "Exclude"

    else:  # c3 c4 c6 c8 c10
        retriever_count += 1
        return "Do not Progress – module retriever"


def get_user():  # Getting user student or staff member
    user_state = input("If you are student enter 's' or if you are staff member enter 't' : ")
    while not (user_state == 's' or user_state == 't'):
        user_state = input("Please enter 's' or 't': ")
    print()
    return user_state


def display_histogram(progress_counter, trailer_counter, retriever_counter, exclude_counter):
    histogram = GraphWin("Histogram", 760, 600)  # Window
    histogram.setBackground(color_rgb(238, 242, 237))

    results_label = Text(Point(190, 30), "Histogram Results")  # Header
    results_label.setStyle('bold')
    results_label.setSize(25)
    results_label.setTextColor(color_rgb(99, 99, 99))
    results_label.draw(histogram)

    x_axis = Line(Point(50, 490), Point(710, 490))  # Drawing x axis
    x_axis.draw(histogram)

    unit_height = 400 / max(progress_counter, trailer_counter, retriever_counter, exclude_counter)
    # Calculating the unit height considering maximum height as 400px

    progress_height = 490 - (progress_counter * unit_height)  # Calculating heights of graphs
    trailer_height = 490 - (trailer_counter * unit_height)
    retriever_height = 490 - (retriever_counter * unit_height)
    exclude_height = 490 - (exclude_counter * unit_height)

    progress_dict = {  # Progress
        "text": "Progress",
        "color": color_rgb(174, 248, 160),
        "height": progress_height,
        "counter": progress_counter
    }

    trailer_dict = {  # Trailer
        "text": "Trailer",
        "color": color_rgb(160, 198, 137),
        "height": trailer_height,
        "counter": trailer_counter
    }

    retriever_dict = {  # Retriever
        "text": "Retriever",
        "color": color_rgb(166, 188, 118),
        "height": retriever_height,
        "counter": retriever_counter
    }

    exclude_dict = {  # Exclude
        "text": "Exclude",
        "color": color_rgb(209, 182, 180),
        "height": exclude_height,
        "counter": exclude_counter
    }

    rectangle_x_start = 85  # Setting initial x coordinates
    text_x = 155

    for i in [progress_dict, trailer_dict, retriever_dict, exclude_dict]:
        number = Text(Point(text_x, i.get("height") - 15), i.get("counter"))  # Counter
        number.setSize(22)
        number.setTextColor(color_rgb(122, 137, 149))
        number.setStyle('bold')
        number.draw(histogram)

        rectangle_x_end = rectangle_x_start + 140

        graph = Rectangle(Point(rectangle_x_start, 490), Point(rectangle_x_end, i.get("height")))  # Graph
        graph.setFill(i.get("color"))
        graph.draw(histogram)

        text = Text(Point(text_x, 510), i.get("text"))  # Text
        text.setStyle('bold')
        text.setSize(22)
        text.setTextColor(color_rgb(117, 133, 145))
        text.draw(histogram)

        rectangle_x_start = rectangle_x_end + 10
        text_x += 150

    total_inputs = progress_counter + trailer_counter + retriever_counter + exclude_counter  # Outcomes
    total_outcome = Text(Point(220, 550), str(total_inputs) + " Outcomes in total.")
    total_outcome.setTextColor(color_rgb(120, 134, 144))
    total_outcome.setSize(24)
    total_outcome.setStyle('bold')
    total_outcome.draw(histogram)

    histogram.getMouse()
    histogram.close()


def access_list(storage):
    for i in range(len(storage)):
        print(storage[i][0] + " - " + str(storage[i][1]) + ", " + str(storage[i][2]) + ", " + str(storage[i][3]))


progress_count = 0  # Setting counts to 0 initially
trailer_count = 0
retriever_count = 0
exclude_count = 0

data_storage = open("credit_data.txt", "w")  # Opening file in write mode

storage_list = []
user = get_user()

while True:

    pass_credit = get_input("pass")  # Getting credits
    while pass_credit is True:  # Getting credit until user enter valid input
        pass_credit = get_input("pass")

    defer_credit = get_input("defer")
    while defer_credit is True:
        defer_credit = get_input("defer")

    fail_credit = get_input("fail")
    while fail_credit is True:
        fail_credit = get_input("fail")

    if pass_credit + defer_credit + fail_credit != 120:  # Checking total
        print("Total incorrect\n")
        continue

    grade = check_grade(pass_credit, defer_credit)  # Part 1A
    print(grade + "\n")

    if user == 's':  # If the user is student program exits
        break

    # Part 2
    data_list = [grade, pass_credit, defer_credit, fail_credit]  # Creating a list to write into a nested list
    storage_list.append(data_list)  # Putting the list into the nested list

    # Part 3
    grade_and_credits = grade + " - " + str(pass_credit) + ", " + str(defer_credit) + ", " + str(fail_credit) + "\n"
    # Creating a string to write to text file
    data_storage.write(grade_and_credits)  # Writing the created string to the text file

    user_input = input("Would you like to enter another set of data?\n"  # Part 1C
                       "Enter 'y' for yes or 'q' to quit and view results: ")
    while not (user_input == 'q' or user_input == 'y'):
        user_input = input("Please enter 'y' or 'q' : ")
    print()

    if user_input == 'q':
        data_storage.close()  # Closing text file in write mode

        try:
            display_histogram(progress_count, trailer_count, retriever_count, exclude_count)  # Part 1D

        except GraphicsError:  # Handling the error caused by quitting histogram using close button
            pass

        # Part 2
        print("Part 2:")
        access_list(storage_list)  # Printing values stored in nested list
        print()

        # Part 3
        print("Part 3:")
        text_input = input("Would you like to print data stored in text file?\n"
                           "Enter 'y' for yes or 'q' to quit : ")
        while not (text_input == 'y' or text_input == 'q'):
            text_input = input("Please enter 'y' or 'q' : ")
        print()

        if text_input == 'y':
            data_viewing = open("credit_data.txt", "r")  # Opening file in read mode
            print(data_viewing.read())  # Printing values stored in text file
            data_viewing.close()  # Closing text file in rea mode
            break

        else:  # text_input == 'q':
            break

    else:  # user_input == 'y':
        continue
