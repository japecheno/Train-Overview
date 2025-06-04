from PrintFunctions import print_additional_menu, print_section_line, print_train_line_list, print_strip_stop_info

file = open("Data/stop_times.txt")
data = file.readlines()

run_program = True

# Option 1 - Overview
def info_overview():
    num_of_total_stops = 0

    train_lines_list = ["BNSF", "HC", "ME", "MD-N", "MD-W", "NCS", "RI", "SWS", "UP-N", "UP-NW", "UP-W"]

    list_of_stops = []

    for line in data[1:]:
        list_of_stops.append(line.strip().split(","))

    # Total Number of Stops
    for stop in list_of_stops:
        num_of_total_stops += 1
    print("Metra has a total of " + str(num_of_total_stops) + " stops")

    # Number of stops for each train line
    for train_line in train_lines_list:
        num_stop_location = 0
        for stop in list_of_stops:
            if train_line in stop[0]:
                num_stop_location += 1
        print(str(train_line) + " has " + str(num_stop_location) + " stops")
    
    print_section_line()

# Option 2 - Search by Train Line
def search_by_train_line(trainline):
    # Creates a list containing every stop
    list_of_stops = []
    
    sorted_stops = []

    # Seperates the list in each individual train stop
    for line in data[1:]:
        list_of_stops.append(line.strip().split(","))

    for stop in list_of_stops:
        if trainline in stop[0]:
            sorted_stops.append(stop)

    # Print list options
    print("----- Trip Display -----")
    print("1) Show all available stops")
    print("2) Show all available trips")
    print_section_line()

    user_input = input("How would you like trip information to be displayed? ")

    if (user_input == "1"):
        print_strip_stop_info(sorted_stops)

    elif (user_input == "2"):
        trip_compile(sorted_stops)

def trip_compile(all_stops):
    i = 0
    current_trip = []
    current_tripid = all_stops[0][0]

    while i < len(all_stops):
        stop = all_stops[i]
        if current_tripid == stop[0]:   # If the trip id matches
            current_trip.append(stop)
        else:
            print("This trip has " + str(len(current_trip)) + " stops which starts at " + current_trip[0][3].strip() + " at " + current_trip[0][1].strip() + " and ends at " + current_trip[len(current_trip) - 1][3].strip() + " at " + current_trip[len(current_trip) - 1][1].strip() + " " + current_trip[0][0])
            current_tripid = stop[0]    # Assigns the new unqiue trip id
            current_trip = [stop]
        i += 1

    print("This trip has " + str(len(current_trip)) + " stops which starts at " + current_trip[0][3].strip() + " at " + current_trip[0][1].strip() + " and ends at " + current_trip[len(current_trip) - 1][3].strip() + " at " + current_trip[len(current_trip) - 1][1].strip())

# Option 3 - Search by Stop Location
def search_by_stop_location(location):
    # Creates a list containing every stop
    list_of_stops = []

    sorted_stops = []

    # Seperates the list in each individual train stop
    for line in data[1:]:
        list_of_stops.append(line.strip().split(","))

    for stop in list_of_stops:
        if location in stop[3]:
            sorted_stops.append(stop)
    
    print_strip_stop_info(sorted_stops)

def additional_sort_menu(option):
    if option == "1":
        pass


# Main


