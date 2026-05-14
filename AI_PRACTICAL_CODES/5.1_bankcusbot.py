# bank_bot.py

import re

# -------------------------
# Helper Functions
# -------------------------

def valid_account(acct):
    return bool(re.fullmatch(r"\d{10}", acct))

def get_balance(acct):
    return f"Balance for {acct}: Rs. 50,000"

def show_loan_info():
    return "Loans available:\nHome: 7.5%\nEducation: 9%\nPersonal: 12%"

def customer_care():
    return "Call: 1800-123-456 or Email: support@bank.com"

# -------------------------
# Response Handler
# -------------------------

def get_response(user_input):

    user_input = user_input.lower().strip()

    if any(x in user_input for x in ['hello', 'hi', 'hey', 'hlo']):
        return "Hi! I'm a bank chatbot."

    elif 'help' in user_input:
        return "Choose options 1-4 from menu."

    elif 'balance' in user_input:
        return "Choose option 1 to check balance."

    elif 'loan' in user_input:
        return show_loan_info()

    elif 'contact' in user_input or 'support' in user_input:
        return customer_care()

    elif any(x in user_input for x in ['thanks', 'thank you', 'thanku']):
        return "You're welcome!"

    elif user_input in ['bye', 'exit']:
        return "Goodbye!"

    return "Invalid input. Choose option 1-4."

# -------------------------
# Menu
# -------------------------

MENU_TEXT = (
    "\nBank Chatbot\n"
    "1. Check Balance\n"
    "2. Loan Info\n"
    "3. Customer Care\n"
    "4. Exit\n"
)

def print_menu():
    print(MENU_TEXT)

# -------------------------
# Main Function
# -------------------------

def main():

    print_menu()

    pending_acct = False

    while True:

        user = input("You: ").strip()

        # Ignore Empty Input
        if not user:
            continue

        # Menu Options
        if user == "1":
            print("Enter account number (10 digits):")
            pending_acct = True
            continue

        elif user == "2":
            print("Bot:", show_loan_info())
            continue

        elif user == "3":
            print("Bot:", customer_care())
            continue

        elif user == "4":
            print("Bot: Goodbye!")
            break

        # Account Number Handling
        if pending_acct:

            if user.lower() == "menu":
                pending_acct = False
                print_menu()

            elif valid_account(user):
                print("Bot:", get_balance(user))
                pending_acct = False

            else:
                print("Bot: Invalid account number")

        else:

            response = get_response(user)

            print("Bot:", response)

            if response == "Goodbye!":
                break

# Driver Code
if __name__ == "__main__":
    main()