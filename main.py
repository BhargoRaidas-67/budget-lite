print("=== MY BUDGET TRACKER ===")

budgetLimit = float(input("Enter your maximum budget ($): "))
totalSpent = 0.0
keepGoing = "yes"

while keepGoing == "yes":
    print("---------------------------------")
    print("Current Total Spent: $", totalSpent)
    
    expense = float(input("Enter your next expense amount ($): "))
    totalSpent = totalSpent + expense
    
    if totalSpent > budgetLimit:
        print("ALERT: You are over your budget limit!")
        
    keepGoing = input("Do you want to add another expense? (yes/no): ")

print("---------------------------------")
print("=== FINAL RESULTS ===")
print("Your budget limit was: $", budgetLimit)
print("Your total spending is: $", totalSpent)

if totalSpent > budgetLimit:
    moneyOver = totalSpent - budgetLimit
    print("You went over budget by: $", moneyOver)

if totalSpent <= budgetLimit:
    moneyLeft = budgetLimit - totalSpent
    print("You have this much leftover: $", moneyLeft)

print("Goodbye!")
