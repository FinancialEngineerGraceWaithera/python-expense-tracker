#created a list called Expenses
expenses = []
#created one item for the list, an expense called food
expense = {
    "category": "Food",
    "amount": 500
}

print(expense)
#added another expense called Transport
expenses.append(expense)

expense = {
    "category": "Transport",
    "amount": 300
}

expenses.append(expense)

print(expenses)
#use a for loop to display the expense category and its amount. 
for expense in expenses:
    print(expense["category"], expense["amount"])
#then proceeded to calculate the total expenses
total = 0

for expense in expenses:
    total = total + expense["amount"]

print("Total:", total)
#And created a prompt to ask for any other expenses eg Rent 20000
category = input("Enter expense category: ").lower()
#Checking what you enetered under category eg Rent
print("You entered:", category)
#Checking the amount you enetered for that category
#input makes Python initially treat the amount you type as a string/text
#Float makes Python see "500" as 500.0
amount = float(input("Enter expense amount: "))

print("Amount entered:", amount)

expense = {
    "category": category,
    "amount": amount
}

expenses.append(expense)

print(expenses)
#We now want Python to keep asking us for expenses until we say we have nothing else to add
#A for loop is useful when we know what we're going through, like:  for expense in expenses: 
# A while loop is useful when we want Python to keep doing something until a condition becomes false
#while = “keep doing this while the condition is true.”
#Now we're going to make the loop actually add expenses.
#We want it to Add expense → ask category → ask amount → save it → ask again
while True:
    choice = input("Do you want to add another expense? (yes/no): ")

    if choice == "no":
        break

#.lower() is a string method that changes letters to lowercase.
    category = input("Enter expense category: ").lower()
    amount = float(input("Enter expense amount: "))

    expense = {
        "category": category,
        "amount": amount
    }
#now let us make the tracker calculate the total 
    expenses.append(expense)

print("\nYour expenses:")

for expense in expenses:
    print(f"{expense['category']}: {expense['amount']:,.0f}")
total = 0

for expense in expenses:
    total = total + expense["amount"]

print(f"Total expenses: {total:,.0f}")
#now we make the tracker more professional by making the output not have the decimal
#change to : print(f"Total expenses: {total:,.0f}")

#I have built a tracker that can:

#✅ Store multiple expenses
#✅ Categorize expenses
#✅ Accept amounts from the user
#✅ Add expenses repeatedly
#✅ Stop when the user enters no
#✅ Calculate the total
#✅ Format the total professionally

#Then we create an expense summary by adding a code before total = 0. Now our expenses are summarised.

#Now we wish to know how much you spent in each category. 
#So lets say you input food twice, 700 and 500, Python will tell you that you spent 1200 on food
category_totals = {}

for expense in expenses:
    category = expense["category"]
    amount = expense["amount"]

    if category in category_totals:
        category_totals[category] = category_totals[category] + amount
    else:
        category_totals[category] = amount

print("\nSpending by category:")

for category, total in category_totals.items():
    print(f"{category}: {total:,.0f}")

#next we add a small budget and compare the budget to the expenses
#monthly budget feature
budget = float(input("Enter your monthly budget: "))
remaining = budget - total
print(f"Budget: {budget:,.0f}")

#What if you spend more than your budget?
if remaining >= 0:
    print(f"Remaining: {remaining:,.0f}")
else:
    print(f"Over budget by: {-remaining:,.0f}")
#Let's make the program tell you how much of your budget you've used.
budget_used = (total / budget) * 100
print(f"Budget used: {budget_used:.1f}%")
#.if means use one decimal place
#your Expense Tracker now has the core features of a small personal finance application
