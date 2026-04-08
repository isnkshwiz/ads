from collections import deque

# BANKkkkk
class BankAccount:
    def __init__(self, account_number, username, balance=0):
        self.account_number = account_number
        self.username = username
        self.balance = balance

    def display(self):
        print(f"{self.username} – Balance: {self.balance}")


# DATA Stuuff
accounts = []  # LinkedList (simulated)
history = []   # Stack (LIFO)
bill_queue = deque()  # Queue (FIFO)
account_requests = deque()

acc_counter = 1


# TSk1
def add_account():
    global acc_counter
    name = input("Enter username: ")
    accounts.append(BankAccount(acc_counter, name, 0))
    acc_counter += 1
    print("Account added successfully")


def display_accounts():
    if not accounts:
        print("No accounts")
        return
    for i, acc in enumerate(accounts, 1):
        print(f"{i}. ", end="")
        acc.display()


def find_account(username):
    for acc in accounts:
        if acc.username == username:
            return acc
    return None


# Task22
def deposit():
    name = input("Enter username: ")
    acc = find_account(name)

    if not acc:
        print("Account not found")
        return

    amount = float(input("Deposit amount: "))
    acc.balance += amount

    history.append(("deposit", name, amount))
    print("New balance:", acc.balance)


def withdraw():
    name = input("Enter username: ")
    acc = find_account(name)

    if not acc:
        print("Account not found")
        return

    amount = float(input("Withdraw amount: "))

    if amount > acc.balance:
        print("Insufficient funds")
        return

    acc.balance -= amount
    history.append(("withdraw", name, amount))
    print("New balance:", acc.balance)


# third task staackk
def show_last_transaction():
    if not history:
        print("No transactions")
    else:
        print("Last:", history[-1])


def undo_transaction():
    if not history:
        print("Nothing to undo")
        return

    action, name, amount = history.pop()
    acc = find_account(name)

    # UNDO!!
    if acc:
        if action == "deposit":
            acc.balance -= amount
        elif action == "withdraw":
            acc.balance += amount

    print("Undo:", action, amount, name)


# Task44 ochered
def add_bill():
    bill = input("Enter bill: ")
    bill_queue.append(bill)
    print("Added:", bill)


def process_bill():
    if not bill_queue:
        print("No bills")
    else:
        print("Processing:", bill_queue.popleft())


def show_bills():
    print("Queue:", list(bill_queue))


# Task55
def request_account():
    global acc_counter
    name = input("Enter username: ")
    account_requests.append(BankAccount(acc_counter, name, 0))
    acc_counter += 1
    print("Request submitted")


def process_request():
    if not account_requests:
        print("No requests")
        return

    acc = account_requests.popleft()
    accounts.append(acc)
    print("Account created for:", acc.username)


def show_requests():
    for acc in account_requests:
        print(acc.username)


# Task6 Arraylum
def array_demo():
    arr = [
        BankAccount(1, "Ali", 150000),
        BankAccount(2, "Sara", 220000),
        BankAccount(3, "John", 100000),
    ]

    for acc in arr:
        acc.display()


# menu in coffee
def bank_menu():
    while True:
        print("\n1. Request Account\n2. Deposit\n3. Withdraw\n4. Back")
        ch = input()

        if ch == "1":
            request_account()
        elif ch == "2":
            deposit()
        elif ch == "3":
            withdraw()
        else:
            break


def atm_menu():
    name = input("Enter username: ")
    acc = find_account(name)

    if not acc:
        print("Not found")
        return

    print("Balance:", acc.balance)

    amount = float(input("Withdraw amount: "))
    if amount <= acc.balance:
        acc.balance -= amount
        print("Withdrawn")
    else:
        print("Insufficient")


def admin_menu():
    while True:
        print("\n1. Process Account\n2. View Requests\n3. View Bills\n4. Back")
        ch = input()

        if ch == "1":
            process_request()
        elif ch == "2":
            show_requests()
        elif ch == "3":
            show_bills()
        else:
            break


# main part of code
def main():
    array_demo()  # Task 6 demo

    while True:
        print("\n1 – Bank\n2 – ATM\n3 – Admin\n4 – Exit")
        choice = input()

        if choice == "1":
            bank_menu()
        elif choice == "2":
            atm_menu()
        elif choice == "3":
            admin_menu()
        else:
            break


if __name__ == "__main__":
    main()