n=int(input("Enter no. of items :"))
whole=0
for i in range(0,n):
    while(True):
        print("Enter Price :",i+1)
        a=int(input())
        if a>0:
            whole=whole+a
            break
        else:
            pass
retail=whole*0.5
print("Retail:",retail)