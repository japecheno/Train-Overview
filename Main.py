from ProgramFunctions import *



def menu():
    while run_program:
        print("----- Metra Tracker -----")
        print("1) Overview")
        print("2) Search by Train Line")
        print("3) Search by Stop Location")
        print("4) Additional Menu")
        print("5) Quit Program")

        user_choice = input("Enter Choice: ")

        print_section_line()

        if user_choice == "1":
            info_overview()

            input("Press enter to return to menu")
            print()



        elif user_choice == "2":
            print_train_line_list()

            train_line = input("Enter Train Line: ")

            search_by_train_line(train_line)

        elif user_choice == "3":
            
            location = input("Enter Location: ")

            search_by_stop_location(location)

        elif user_choice == "4":
            print_additional_menu()

            other_tools = input("Which tool would you like to use?: ")

            additional_sort_menu(other_tools)


        elif user_choice == "5":
            print("Exiting Program...")
            break

        else:
            print("Not a valid input")

menu()