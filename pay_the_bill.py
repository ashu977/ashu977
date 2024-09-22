import random
a=input("enter everybody's name separated by comma:")
b=a.split(" ")
d=len(b)
c=random.randint(0,d-1)
print(f"{b[c]} will pay the bill.")