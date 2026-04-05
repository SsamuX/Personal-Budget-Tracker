def get_budget_data():
    income = float(input("Enter total income: "))
    food = float(input("Enter food expense: "))
    transport = float(input("Enter transport expense: "))
    rent = float(input("Enter rent expense: "))
    entertainment = float(input("Enter entertainment expense: "))

    expenses = [food, transport, rent, entertainment]
    return income, expenses
