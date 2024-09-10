# Dictionary to store reservations
reservations = {}

# Function to make a reservation
def make_reservation():
    print("\nEnter the following details to book a reservation:")
    name = input("Name: ")
    date = input("Date (DD/MM/YYYY): ")
    total_members = input("Total Members: ")
    room_no = input("Room Number: ")
    id_number = input("ID Number: ")

    reservation_id = len(reservations) + 1  # Auto-generate reservation ID
    reservations[reservation_id] = {
        "Name": name,
        "Date": date,
        "Total Members": total_members,
        "Room Number": room_no,
        "ID Number": id_number
    }

    print(f"\nReservation successful! Your reservation ID is {reservation_id}\n")

# Function to view all reservations
def view_reservations():
    if reservations:
        print("\nCurrent Reservations:")
        for res_id, details in reservations.items():
            print(f"\nReservation ID: {res_id}")
            for key, value in details.items():
                print(f"{key}: {value}")
            print("-" * 30)  # Line separator between reservations
    else:
        print("\nNo reservations found.\n")

# Function to cancel a reservation
def cancel_reservation():
    if reservations:
        reservation_id = int(input("\nEnter the Reservation ID to cancel: "))
        if reservation_id in reservations:
            del reservations[reservation_id]
            print(f"Reservation ID {reservation_id} has been cancelled.\n")
        else:
            print("Invalid Reservation ID.\n")
    else:
        print("No reservations to cancel.\n")

# Main function to display options
def main_menu():
    while True:
        print("\n--- Online Reservation System ---")
        print("1. Make a Reservation")
        print("2. View Reservations")
        print("3. Cancel a Reservation")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            make_reservation()
        elif choice == "2":
            view_reservations()
        elif choice == "3":
            cancel_reservation()
        elif choice == "4":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Running the system
if __name__ == "__main__":
    main_menu()
