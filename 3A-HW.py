income = input("Type income: ")
expense = input("Type expense: ")
profit = int(income) - int(expense)

def person ():
    if income >= 5000:
        print("You're a high income earner.")
    elif income >= 3000 and income < 5000:
        print("You're an average income earner.")
    else:
        print("You're a low income earner.")
        
print("Your profit is: ", profit)