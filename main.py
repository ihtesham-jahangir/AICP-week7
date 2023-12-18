# Constants
NUM_CHARITIES = 3

# Initialize charity names and donation totals
charity_names = ["Charity 1", "Charity 2", "Charity 3"]
charity_totals = [0] * NUM_CHARITIES

# Function to set up the donation system
def setup_donation_system():
    print("TASK 1: Set up the donation system")
    for i in range(NUM_CHARITIES):
        print(f"{i+1}. {charity_names[i]}")
    while True:
        choice = int(input("Enter the number (1/2/3) to choose a charity: "))
        if 1 <= choice <= NUM_CHARITIES:
            return choice
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

# Function to record and total each donation
def record_donation():
    print("\nTASK 2: Record and total each donation")
    choice = setup_donation_system()
    bill_amount = float(input("Enter the customer's shopping bill amount: "))
    donation = bill_amount * 0.01
    charity_totals[choice - 1] += donation
    print(f"Donation to {charity_names[choice - 1]}: ${donation:.2f}")

# Function to show the totals so far
def show_totals():
    print("\nTASK 3: Show the totals so far")
    grand_total = 0
    sorted_charities = sorted(enumerate(charity_totals, start=1), key=lambda x: x[1], reverse=True)
    
    for idx, total in sorted_charities:
        print(f"{charity_names[idx - 1]}: ${total:.2f}")
        grand_total += total
    
    print(f"\nGRAND TOTAL DONATED TO CHARITY: ${grand_total:.2f}")

# Main program
while True:
    choice = int(input("\nEnter your choice (1/2/3, -1 to show totals, 0 to exit): "))
    
    if choice == 1:
        record_donation()
    elif choice == 2:
        record_donation()
    elif choice == 3:
        record_donation()
    elif choice == -1:
        show_totals()
    elif choice == 0:
        print("Exiting the program. Thank you!")
        break
    else:
        print("Invalid choice. Please choose 1, 2, 3, -1, or 0.")
