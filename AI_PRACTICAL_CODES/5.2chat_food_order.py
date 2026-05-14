menu = {
    "burger": 59.9,
    "pizza": 89.9,
    "pasta": 74.9,
    "salad": 44.9,
    "soda": 19.9,
    "coffee": 25.0
}

def greet_user():
    print("Hello! Welcome to the Food Service Chatbot!")
    print("I can help you with the menu, take your order, or give you information.")
    print("Type 'help' for assistance at any time.")

def show_menu():
    print("\nHere is our menu:")
    for item, price in menu.items():
        print(f"{item.capitalize()}: Rs.{price:.2f}")

def take_order():
    order = {}
    while True:
        item = input("\nWhat would you like to order? (Type 'done' when finished): ").lower()
        if item == "done":
            break
        elif item in menu:
            try:
                quantity = int(input(f"How many {item}s would you like? "))
                if item in order:
                    order[item] += quantity
                else:
                    order[item] = quantity
                print(f"{quantity} {item}(s) added to your order.")
            except ValueError:
                print("Please enter a valid quantity.")
        else:
            print("Sorry, we don't have that item. Please choose from the menu.")
    return order

def calculate_total(order):
    total = 0
    for item, quantity in order.items():
        total += menu[item] * quantity
    return total

def handle_user_input():
    order = {}  # Initialize order variable here
    while True:
        user_input = input("\nHow can I assist you today? (Type 'help' for options): ").lower()
        if user_input == "help":
            print("\nYou can ask me the following things:")
            print("'menu' - to see the menu")
            print("'order' - to place an order")
            print("'exit' - to exit the chatbot")
            print("'total' - to see your current order total")
        elif user_input == "menu":
            show_menu()
        elif user_input == "order":
            order = take_order()
            print(f"\nYour current order is: {order}")
            total = calculate_total(order)
            print(f"Your total is: Rs.{total:.2f}")
        elif user_input == "exit":
            print("Thank you for using our chatbot! Have a great day!")
            exit()
        elif user_input == "total":
            if not order:
                print("Please place an order first to calculate the total.")
            else:
                total = calculate_total(order)
                print(f"Your total is: Rs.{total:.2f}")
        else:
            print("Sorry, I didn't understand that. Type 'help' for options.")

def main():
    greet_user()
    handle_user_input()

if __name__ == "__main__":

    main()