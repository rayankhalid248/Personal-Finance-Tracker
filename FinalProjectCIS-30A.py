# ------------------------------------
# Project: Personal Finance Tracker
# Programmer: Rayan Khalid
# CIS-30 A
#-------------------------------------
# monthly budget

import finance_tools

# Classes
class Transaction:

    # constructor
    def __init__(self, amount, category):

        # storing data
        self.amount = amount
        self.category = category

    # display transaction
    def display(self):

        print("Amount: $", self.amount)
        print("Category: ", self.category)

class Budget:

    # constructor
    def __init__(self, limit):

        self.limit = limit

    def display_budget(self):

        print("Budget Limit: $", self.limit)

# subclass that inherits from Transaction
class Expense(Transaction):

    # constructor
    def __init__(self, amount, category, description):

        # call parent class constructor
        super().__init__(amount, category)

        # store description
        self.description = description

    # display expense
    def display_expense(self):

        print("Expense Amount: $", self.amount)
        print("Category:", self.category)
        print("Description:", self.description)

# list for storing Expense objects
expense_objects = []

budget = 0

# amount of income
income = 0

# amount of expenses
expenses = 0

# objects
user_budget = Budget(budget)

# list of expenses
expense_list = []

# Ask user for the budget
try:

    # Convert user input into a number
    budget = float(input("Enter your monthly budget: $"))
    user_budget.limit = budget

except ValueError:

    # Runs if the user enters letters
    print("Invalid input. Budget set to 0.")

    budget = 0

# Function for adding income
def add_income():

    global income

    try:

        # Ask the user for income amount
        amount = float(input("Enter income amount: "))

        # Add income to total
        income = income + amount

        print("Income added.")

    except ValueError:

        print("Invalid input. Please enter a number.")

# Function for adding expenses
def add_expense():

    global expenses

    try:

        # Ask user for expense amount
        amount = float(input("Enter expense amount: $"))
        if amount < 0:

            print("Expense cannot be negative.")
            return

        # Add expense to total
        expenses = expenses + amount

        # Save expense in list
        expense_list.append(amount)

        # Ask for expense details
        category = input("Enter expense category: ")

        description = input("Enter expense description: ")

        # Create Expense object
        new_expense = Expense(amount,category,description)

        # Store object
        expense_objects.append(new_expense)

        print("Expense added.")

    except ValueError:

        print("Invalid input. Please enter a number.")

# function for saving all the info into a text file
def save_file():

    # find how much money is left
    remaining = finance_tools.calculate_remaining(income, expenses)

    # open a file called summary.txt
    try:

        # open the file
        import os

        file_path = os.path.join(os.path.dirname(__file__), "summary.txt")
        file = open(file_path, "w")

        # Write the info into the file
        file.write("------ Financial Summary ------\n")
        file.write("Budget: $" + str(budget) + "\n")
        file.write("Income: $" + str(income) + "\n")
        file.write("Expenses: $" + str(expenses) + "\n")
        file.write("\nExpenses Entered:\n")

        # counter for numbering expenses
        number = 1

        # use a loop to go through the expense list
        for amount in expense_list:

            # write each expense into the file
            file.write("Expense " + str(number) + ": $" + str(amount) + "\n")

            # increase counter
            number = number + 1

        # write the remaining amount
        file.write("\nMoney left: $" + str(remaining))

        # close file
        file.close()
        print("Summary was saved to the file")

    except IOError:

        print("Could not save file.")

# function for displaying financial info
def display_summary():

    # finding how much money remains
    remaining = finance_tools.calculate_remaining(income,expenses)

    print()

    # display all info gathered
    print("Financial Summary")
    print("Budget: $", budget)
    print("Income: $", income)
    print("Expenses: $", expenses)
    print("Money Left: $", remaining)

    print()
    print("Expenses Entered: ")

    # counter to number each expense
    number = 1

    # loop through every expense in the expense list
    for amount in expense_list:

        print("Expense", number, ": $", amount)

        # add 1 to the counter
        number = number + 1

    # Check budget status
    message = finance_tools.check_budget(budget, expenses)

    print(message)

# Menu
# variable that stores the user's choice
choice = 0

while choice != 5:

    print("Personal Finance Tracker")

    # Menu options
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Summary")
    print("4. Save to File")
    print("5. Exit")

    # ask the user to enter a number 1-5
    try:

        # Get menu choice
        choice = int(input("Enter your choice (1-5): "))

    except ValueError:

        print("Please enter a number.")

        choice = 0

    # Option 1: call add_income function
    if choice == 1:
        add_income()

    # Option 2: call add_expense() function
    elif choice == 2:
        add_expense()

    # Option 3: call display_summary
    elif choice == 3:
        display_summary()

    # Option 4: call save_file
    elif choice == 4:
        save_file()

    # Option 5: Goodbye Message
    elif choice == 5:
        print("Thank you!")

    # Option 6: User enters a number that isn't 1-5
    else:
        print("Invalid number. Has to be 1-5. Try again")

