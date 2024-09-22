pizza = str(input("which size do you want to order?\n small\n medium\n large "))
bill = 0
if pizza == "small":
    bill += 100
    print("the price of pizza is 100 Rs.")
elif pizza == "medium":
    bill += 200
    print("the price of pizza is 200 Rs.")
else:
    bill += 300
    print("the price of pizza is 300 Rs.")

a = input("would you like to add pepperoni?(Y/N)")
if a == "y" or a == "Y":
    if pizza == "small":
        bill += 30
    elif pizza == "medium" or pizza == "large":
        bill += 50

b = input("would you to add extra cheese?(Y/N)")
if b == "Y" or b == "y":
    bill += 20

print(f"your total bill is {bill}")
