#create function for income bracket with if-else statement
def IncomeBracket (income):
    if income >= 5000: 
        return "High income earner"
    elif income >= 3000 and income < 5000:
        return "Average income earner"
    else:
        return "Low income earner"
#create function for profit
def Profit(income, expense):
  return income - expense
#declare variables 
names = []
profits = []
choice = "y"
#construct requirements for user input with control loops
while choice == "y":
  name = input("Enter name: ");
  income = int(input("Type income: "))
  expense = int(input("Type expense: "))
 
  profit = Profit(income, expense)
  print("Your profit is: ", profit)
 
  names.append(name)
  profits.append(profit)
  choice = input("\nDo you want to input another entry? (y/n)")
  print("\n")
 
for i in range(len(names)):
  print(f"Name: {names[i]}\tProfit: {profits[i]}\tIncome Bracket: {IncomeBracket(profits[i])}")
