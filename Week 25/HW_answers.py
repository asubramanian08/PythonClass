money = 0
GOAL = 20
while money < GOAL:
    print("Keep working toward your goal of", GOAL, "dollars")
    newDollars = int(input("Enter how much money you have: "))
    if money > newDollars:
        print("Poor money management.", "You lost",
              money - newDollars, "dollars")
        break
    money = newDollars
    print("You have", money, "dollars in your bank account.")
if money >= 20:
    print("You have reached your financial goal of", GOAL, "dollars!")
