def get_warning_message(balance):
    if balance < 0:
        return "Warning: You have overspent."
    elif balance == 0:
        return "Caution: Your balance is zero."
    else:
        return "Good job: Your spending is within your budget."
