a=int(input("Enter a five digit number:"))
while a>0:
    temp=a%10
    a=a//10
    print(temp)
