# greater number
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a second number: "))
if(num1 > num2):
    print("the first number is greater")
elif (num1 < num2):
    print("the second number is greater")
else:
    print("the two numbers are the same")

# sum of numbers less then the reference
ref = 10
s = 0
for i in range(10):
    res = int(input("Enter a number: "))
    if res == ref:
        break
    if res < ref:
        s += res
print("The sum of the numbers less then", ref, "is", s)
