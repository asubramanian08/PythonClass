COUNT_TILL = 10
enteredCorrectly = True
print("Enter all number from 1 till", COUNT_TILL, "in order")
for i in range(COUNT_TILL):
    if int(input()) != i + 1:
        print("Wrong input, you should have entered", i)
        enteredCorrectly = False
        break
if enteredCorrectly:
    print("You entered all the numbers till", COUNT_TILL, "correctly!")
