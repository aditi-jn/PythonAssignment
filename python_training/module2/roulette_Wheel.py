num=int(input("Enter a Pocket Number:"))
if num==0:
    print("Green")
elif num<=10:
    if num%2==0:
        print("Black")
    else:
        print("Red")
elif num<=18:
    if num % 2 == 0:
        print("Red")
    else:
        print("Black")
elif num<=28:
    if num % 2 == 0:
        print("Black")
    else:
        print("Red")
elif num<=36:
    if num % 2 == 0:
        print("Black")
    else:
        print("Red")
else :
    print("Sorry you have entered pocket number is out of range")