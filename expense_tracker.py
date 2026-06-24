expenses = []


def load_expenses():
    try:
        with open("expenses.txt", "r") as file:
            
            for line in file:
                data= line.strip().split(",")
                expense = {
                    "amount": float(data[0]),
                    "category": data[1]
                }

                expenses.append(expense)

    except FileNotFoundError:
        pass

def save_expenses():
    with open("expenses.txt", "w") as file:

        for expense in expenses:
            file.write(
                str(expense["amount"])
                + ","
                + expense["category"]
                + "\n"
            )

def add_expense():
    amount = float(input("Enter Amount: "))
    category = input("Enter Category: ")

    expense = {
        "amount": amount,
        "category": category
    }
    expenses.append(expense)
    save_expenses()
    print("Expense Added Successfully!")

def view_expenses():
    if len(expenses) == 0:
        print("No Expenses Found!")
    else:
        print("\nExpenses:")
        for i, expense in enumerate(expenses, start=1):

            print(
                i,
                "| Amount:", expense["amount"],
                "| Category:", expense["category"]

            )

def show_total():
    total = 0

    for expense in expenses:
        total += expense["amount"]
    print("Total Expense:", total)

def delete_expense():
    view_expenses

    if len(expenses) == 0:
        return
    
    index = int(input("Enter Expense Number to Delete: "))

    if 1 <= index <= len(expenses):

        expenses.pop(index - 1)

        save_expenses()
        print("Expenses Deleted Successfully!")

    else:
        print("Invalid Number!")

def search_expense():

    category = input("Enter Category to Search:")

    found = False

    for expense in expenses:

        if expense["category"].lower() == category.lower():

            print(
                "Amount:",
                expense["amount"],
                " | Category:",
                expense["category"]
            )

            found = True

    if not found:
        print("No Expense Found!")

load_expenses()

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Show Total Expense")
    print("4. Delete Expense")
    print("5. Search Expense")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        show_total()
            
    elif choice == "4":
        delete_expense()

    elif choice == "5":
        search_expense()

    elif choice == "6":
        print("Program Closed")
        break

    else:
        print("Invalid Choice!")
