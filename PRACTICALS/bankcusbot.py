# bank_bot.py
"""
Bank Virtual Assistant - NLTK implementation (simple, offline, simulated).
Requirements:
  pip install nltk
This script uses nltk.chat.util.Chat for conversational replies,
but the main menu and account actions are handled by the program logic.
"""

import re
import hashlib
import random
from datetime import datetime, timedelta

try:
    from nltk.chat.util import Chat, reflections
except Exception as e:
    raise SystemExit("nltk not found. Install with: pip install nltk")

# -------------------------
# Helper (simulated) bank functions
# -------------------------
def valid_account(acct: str) -> bool:
    """Validate account number (simple rule: exactly 10 digits)."""
    return bool(re.fullmatch(r"\d{10}", acct))

def deterministic_random_from_key(key: str):
    """Return a random.Random seeded deterministically from a key string."""
    seed = int(hashlib.sha256(key.encode()).hexdigest(), 16)
    return random.Random(seed)

def get_balance(acct: str) -> str:
    """Return a deterministic fake balance for an account number."""
    rnd = deterministic_random_from_key("balance:" + acct)
    amount = rnd.randint(5000, 5000000) / 100.0  # rupees.xx
    return f"Account {acct} — Available balance: ₹{amount:,.2f}"

def get_mini_statement(acct: str, n: int = 5) -> str:
    """Generate a deterministic last-n transactions list."""
    rnd = deterministic_random_from_key("mini:" + acct)
    lines = []
    today = datetime.today()
    for i in range(n):
        # Date decreasing by 1..n days
        date = (today - timedelta(days=i)).strftime("%Y-%m-%d")
        txn_type = rnd.choice(["CR", "DR"])
        amt = rnd.randint(100, 50000) / 100.0
        desc = rnd.choice([
            "ATM withdrawal", "UPI payment", "Salary", "Utility bill",
            "Grocery", "POS purchase", "EMI payment", "Refund"
        ])
        lines.append(f"{date} | {txn_type} | ₹{amt:,.2f} | {desc}")
    return "Last 5 transactions for account " + acct + ":\n" + "\n".join(lines)

def show_loan_info() -> str:
    """Return static loan types and sample interest rates."""
    return (
        "Available loans:\n"
        "- Home Loan: 7.35% p.a. (example rate)\n"
        "- Education Loan: 9.00% p.a. (example rate)\n"
        "- Personal Loan: 12.75% p.a. (example rate)\n"
        "Note: Rates are illustrative. Contact bank for exact rates."
    )

def get_card_balance(acct: str) -> str:
    """Simulated credit-card balance tied to account number."""
    rnd = deterministic_random_from_key("card:" + acct)
    bal = rnd.randint(0, 200000) / 100.0
    return f"Credit card linked to {acct} — Outstanding balance: ₹{bal:,.2f}"

def report_lost_card(acct: str) -> str:
    """Simulate reporting a lost card and return a reference id."""
    rnd = deterministic_random_from_key("report:" + acct)
    ref = hex(rnd.randint(0x10000, 0xFFFFFF))[2:].upper()
    return f"Lost-card reported for account {acct}. Reference ID: RPT-{ref}"

def customer_care() -> str:
    return "Customer Care: Phone: 1800-123-456 | Email: support@bank.example"

# -------------------------
# NLTK Chat pairs
# -------------------------
pairs = [
    (r'hi|hello|hey', ["Hello! I'm your Bank Virtual Assistant. How can I help?"]),
    (r'help', ["You can type a menu number (1-6) or say 'check balance', 'mini statement', 'loan', 'credit card', 'customer care', or 'exit'."]),
    (r'check balance', ["To check balance, enter menu option 1 or type your 10-digit account number when prompted."]),
    (r'mini statement|mini-statement|statement', ["To view mini statement, enter menu option 2."]),
    (r'loan|loan info|loan information', [show_loan_info()]),
    (r'credit card|card', ["For credit card services, enter menu option 4."]),
    (r'customer care|contact|support', [customer_care()]),
    (r'exit|quit|bye', ["Goodbye! Thank you for using the Bank Virtual Assistant."]),
    (r'.*', ["I'm here. Choose a menu option (1-6) or ask 'help' for guidance."])
]
chat = Chat(pairs, reflections)

# -------------------------
# Main menu-driven loop
# -------------------------
MENU_TEXT = (
    "Welcome to Bank Virtual Assistant\n"
    "Menu:\n"
    "1. Check Balance\n"
    "2. Mini Statement\n"
    "3. Loan Information\n"
    "4. Credit Card Services\n"
    "5. Customer Care\n"
    "6. Exit\n"
)

def print_menu():
    print("-" * 40)
    print(MENU_TEXT)
    print("You may also type a phrase like 'check balance' or 'help'.")
    print("-" * 40)

def main():
    print_menu()
    pending_action = None  # None or one of: 'balance', 'mini', 'card_balance', 'report_card'
    while True:
        try:
            user = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break

        # numeric menu shortcut
        if re.fullmatch(r"[1-6]", user):
            choice = user
            pending_action = None
            if choice == "1":
                pending_action = "balance"
                print("Bot: Please enter your 10-digit account number:")
                continue
            elif choice == "2":
                pending_action = "mini"
                print("Bot: Please enter your 10-digit account number:")
                continue
            elif choice == "3":
                print("Bot:", show_loan_info())
                continue
            elif choice == "4":
                # sub-menu for credit-card
                print("Bot: Credit Card Services — choose:")
                print("  a) Check credit card balance")
                print("  b) Report lost card")
                sub = input("You (a/b): ").strip().lower()
                if sub == "a":
                    pending_action = "card_balance"
                    print("Bot: Please enter your 10-digit account number linked to the card:")
                    continue
                elif sub == "b":
                    pending_action = "report_card"
                    print("Bot: Please enter your 10-digit account number linked to the card:")
                    continue
                else:
                    print("Bot: Invalid choice in credit-card menu.")
                    continue
            elif choice == "5":
                print("Bot:", customer_care())
                continue
            elif choice == "6":
                print("Bot: Goodbye! Thank you for using the Bank Virtual Assistant.")
                break

        # if an account number is expected and user supplied digits
        if pending_action and valid_account(user):
            acct = user
            if pending_action == "balance":
                print("Bot:", get_balance(acct))
            elif pending_action == "mini":
                print("Bot:", get_mini_statement(acct, n=5))
            elif pending_action == "card_balance":
                print("Bot:", get_card_balance(acct))
            elif pending_action == "report_card":
                print("Bot:", report_lost_card(acct))
            else:
                print("Bot: Action not recognized.")
            pending_action = None
            continue
        elif pending_action and not valid_account(user):
            print("Bot: Invalid account number. Please enter a 10-digit number (or type 'cancel').")
            if user.lower() == "cancel":
                pending_action = None
            continue

        # Fallback to NLTK chat for natural language replies
        response = chat.respond(user)
        # Chat.respond might return None sometimes; guard against that.
        if response:
            print("Bot:", response)
            # if response suggests exit, break
            if re.search(r'goodbye|thank you', response, re.I):
                break
        else:
            print("Bot: Sorry, I didn't understand. Type 'help' or choose 1-6 from the menu.")

if __name__ == "__main__":
    main()