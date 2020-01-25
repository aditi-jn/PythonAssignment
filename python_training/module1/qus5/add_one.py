a=int(input("Enter a five digit number:"))
while a>0:
    temp=a%10
    temp=temp+1
    a=a//10
    print(temp)
