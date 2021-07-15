# if statements
num = int(input("Enter a number: "))
if num > 0:
    print("positive")
elif num < 0:
    print("negative")
else:
    print("zero")

# logic statements
ps5_cost = 500
ps5_available = False
wallet = 200  # i'm broke
momPays = True
if ps5_available and (ps5_cost < wallet or momPays):
    print("Can buy ps5")
else:
    print("Can't buy ps5")

# break and continue
s = "Hi0 m0y0 0n0am0e0 is0 0Bo0b0"
for ch in s:
    if ch == '0':
        break
    print(ch, end='')
print()
for ch in s:
    if ch == '0':
        continue
    print(ch, end='')
print()

# pass
for ch in s:  # note: same as prev loop
    if ch == '0':
        pass
    else:
        print(ch, end='')
