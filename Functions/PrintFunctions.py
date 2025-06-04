# Print Functions

def print_section_line():
    print("--------------------")

def print_train_line_list():
    print("----- Train Lines -----")
    print("BNSF (BNSF)")
    print("Heritage Corridor (HC)")
    print("Metra Electric (ME)")
    print("Milwaukee District North (MD-N)")
    print("Milwaukee District West (MD-W)")
    print("Nort Central Service (NCS)")
    print("Rock Island (RI)")
    print("Southwest Service (SWS)")
    print("Union Pacific Northwest (UP-NW)")
    print("Union Pacific West (UP-W)")
    print_section_line()

def print_additional_menu():
    print("----- Addition Menu -----")
    print("1) Find trips by tripid element")

def print_strip_stop_info(sorted_stops):
    for stop in sorted_stops:
        print("Trip Id: " + str(stop[0]) + " " + str(stop[1][:7]) + " " + str(stop[3]))