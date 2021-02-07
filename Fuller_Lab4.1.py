# David Fuller
# Complete
# Get budget and compare to aggregate expenses

budget = int(input("Enter amount budgeted for the month: "))
expense = 1
total_expense = 0
while expense != 0:
    expense = int(input("Enter an amount spent(0 to quit): "))
    total_expense += expense
print("Budgeted: $", format(budget, ',.2f'))
print("Spent: $", format(total_expense, ',.2f'))
if budget >= total_expense:
    print("Great job! You are $", format(budget - total_expense, ',.2f'), " under budget!")
else:
    print("You are $", (format(abs(budget - total_expense), ',.2f')),"over budget. PLAN BETTER NEXT TIME!")
