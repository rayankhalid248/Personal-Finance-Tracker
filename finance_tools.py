# ------------------------------------
# Project: Personal Finance Tracker
# Programmer: Rayan Khalid
# CIS-30 A
#-------------------------------------

print("finance_tools.py is running")


# Function to calculate remaining money
def calculate_remaining(income, expenses):

    # subtract expenses from income
    remaining = income - expenses

    # return result
    return remaining


# Function to check budget status
def check_budget(budget, expenses):

    # check if expenses exceed budget
    if expenses > budget:

        return "You are over budget."

    # check if expenses equal budget
    elif expenses == budget:

        return "You have reached your budget limit."

    # otherwise
    else:

        return "You are within your budget."