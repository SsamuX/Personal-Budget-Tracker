from input_handler import get_budget_data
from calculator import calculate_total_expenses, calculate_balance
from warnings import get_warning_message


def main():
    income, expenses = get_budget_data()

    total_expenses = calculate_total_expenses(expenses)
    balance = calculate_balance(income, total_expenses)
    message = get_warning_message(balance)

    print("\n----- PERSONAL BUDGET REPORT -----")
    print("Income:", income)
    print("Total Expenses:", total_expenses)
    print("Balance:", balance)
    print("Message:", message)


main()
