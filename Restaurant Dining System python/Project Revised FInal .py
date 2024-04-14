from tabulate import tabulate
import os

MakeReservation = []

# Function to clear the console screen based on the operating system
def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to display the main system menu
def SystemMenu():
    clearScreen()
    print("""
          RESTAURANT DINING RESERVATION SYSTEM
                SYSTEM MENU 
                 
                a. View all Reservations 
                b. Make a Reservation
                c. Delete a Reservation
                d. Generate Reservation Report
                e. Exit application
          """)

# Function to view all reservations
def ViewReservations():
    clearScreen()  
    tabledata = []

    # Display reservations in table
    if MakeReservation:
        for i, reservation in enumerate(MakeReservation, start=1):
            # Create a row for reserve
            row = [i, reservation['date'], reservation['time'], reservation['name'], reservation['adults'],
                   reservation['children']]
            tabledata.append(row)

        # Generate and display the table using the tabulate library
        table = tabulate(tabledata, headers=["#", "Date", "Time", "Name", "Adults", "Children"], tablefmt="grid", numalign="center", stralign="center")
        print(table)
        input('Press ENTER to continue...')

        with open('Information.txt', 'a') as file:
            file.write(table)
            file.write("\n")

    else:
        print("No Reservations")
        input("Enter to continue")

# Function to delete a reservation
def DeleteReservation():
    clearScreen()
    while True:
        try:
    
            NumReservation = int(input("Enter a number from the list to delete or enter a negative value to cancel "))
            
            # Delete the reservation if the input is valid only under sa greater than 1 and less than sa reservation 
            if NumReservation >= 1 and NumReservation <= len(MakeReservation):
                MakeReservation.pop(NumReservation - 1)
                print("Successfully deleted:")
                print("Deleted Reservation:")

            # If the input is negative it will exit
            elif NumReservation < 0 or NumReservation > len(MakeReservation):
                print("Cancelled. No reservation deleted.")
                break
            else:
                print("Invalid input. Please enter a valid number.")
        except ValueError:
            print("It should be numbers")

# Function to make a reservation
def MakeReservationFunction():
    clearScreen()
    if len (MakeReservation) >= 100:
        print('Reservation limit reached')
        input('Press ENTER to continue...')
        return
    
    while True:
        try:
            Name = input("Enter your name: ")
            Date = input("Enter date: ")
            Time = input("Enter time: ")
            Adults = int(input("Enter No of adults: "))
            Children = int(input("Enter No of Children: "))

            # Create a dictionary for the reservation and add it to the list
            AllReservation = {
                'name': Name,
                'date': Date,
                'time': Time,
                'adults': Adults,
                'children': Children
            }
            MakeReservation.append(AllReservation)

            print("Reservation successfully added!")
            input('Press ENTER to continue...')
            break
        except ValueError as e:
            print(f"Error: {e}. Please enter valid numerical values for adults and children.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

def GenerateReservationReport():
    clearScreen()
    TotalCost = 0
    TotalAdults = 0
    TotalKids = 0
    tabledata = []

    if MakeReservation: 
     for i, reservation in enumerate(MakeReservation, start=1):  # for loop through reservations to (calculate total cost) also to display
        TotalAdultsCost = reservation['adults'] * 500
        TotalChildrenCost = reservation['children'] * 300
        TotCost1 = TotalAdultsCost + TotalChildrenCost
        TotalCost += TotCost1 
        TotalAdults += reservation['adults']
        TotalKids += reservation['children']
        row = [i, reservation['date'], reservation['time'], reservation['name'], reservation['adults'],
               reservation['children'], TotCost1]
        tabledata.append(row)

        # Display the table using the tabulate library
        table = tabulate(tabledata, headers=["#", "Date", "Time", "Name", "Adults", "Children", "Subtotal"], tablefmt="grid", numalign="center", stralign="center")
        print(table)
        print("")
        print(f"Total Number of Adults: {TotalAdults}")
        print(f"Total Number of Kids: {TotalKids}")
        print(f"Total Cost of all reservations: PHP {TotalCost}")
        input('Press ENTER to continue...')

        # txt filee
        with open('Information.txt', 'a') as file:
            file.write(table)
            file.write(f"\nTotal Number of Adults: {TotalAdults}")
            file.write(f"\nTotal Number of Kids: {TotalKids}")
            file.write(f"\nTotal Cost of all reservations: PHP {TotalCost}\n")
    else:
        print("No Reservations")
        input("Enter to continue")
        
# Main loop for application
while True:
    SystemMenu()
    print()
    Menu = input("Choose a letter: ").lower()
    print()

    # just the options 
    if Menu == "a":
        ViewReservations()
    elif Menu == "b":
        MakeReservationFunction()
    elif Menu == "c":
        DeleteReservation()
    elif Menu == "d":
        GenerateReservationReport()
    elif Menu == "e":
        break
    else:
        print("Error. Enter another")
