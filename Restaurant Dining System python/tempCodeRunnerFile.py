MakeReservation = []

def MakeReservationFunction():
    while True:
        try:
            Name = input("Enter your name: ")
            Date = input("Enter date: ")
            Time = input("Enter time: ")
            Adults = int(input("Enter No of adults: "))
            Children = int(input("Enter No of Children: "))

            AllReservation = {
                'name': Name,
                'date': Date,
                'time': Time,
                'adults': Adults,
                'children': Children
            }
            MakeReservation.append(AllReservation)

            with open('Information.txt', 'a') as file:
                if file.tell() == 0:
                    file.write(f"{'#':<1} {'Date':<15} {'Time':<15} {'Name':<20} {'Adults':<6} {'Children':<9}\n")

                index = len(MakeReservation) - 1        
                file.write(f"{index + 1:<1}\t{Date:<15}\t{Time:<15}\t{Name[:20]:<20}\t{Adults:<6}\t{Children:<9}\n")

            print("Reservation successfully added!")
            break
        except ValueError as e:
            print(f"Error: {e}. Please enter valid numerical values for adults and children.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            