import random

a=(input("enter your choice (R/P/S)"))
c=a.lower()
if a=='r':
    print("🪨")
elif a=='p':
    print("🧻")
elif a=='s':
    print("✂️")
l=[0,1,2]
b=random.choice(l)
if b==0:
    print("🪨")
elif b==1:
    print("🧻")
elif b==2:
    print("✂️")
if b==0 and c=='r':
    print("tie")
elif b==0 and c=='p':
    print("you win.")
elif b==0 and c=='s':
    print("you lose.")
elif b==1 and c=='p':
    print("tie")
elif b==1 and c=='r':
    print("you loose.")
elif b==1 and c=='s':
    print("you win.")
elif b==2 and c=='s':
    print("tie")
elif b==2 and c=='p':
    print("you loose.")
elif b==2 and c=='r':
    print("you win.")
print("thanks for playing.")
