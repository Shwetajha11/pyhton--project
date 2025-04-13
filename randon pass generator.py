##PROJECT- creating code for automatic password and email generator
#with the help of user's name
'''Why This is Useful
Ensures consistency and uniqueness in email creation.

Creates secure passwords combining user-specific input and randomness.

Helpful in automating onboarding or registration processes.'''
import random

w={}
while True:
    q=input("enter your name")
    print(q+"@gmail.com")
    c="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*()"
    y=""

    for i in range(8):
        a=random.randint(0,len(c))
        y=y+c[a]
    print("password",y)
    w[q]=y
    ch=input("press Y to continue")
    if ch!="Y":
        break

print(w)
    
