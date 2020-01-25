name='PRACHI'

for k in range(0,len(name)):
    word = input("\nEnter one word in your name")
    if word=='P':
        p=[1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,0,0,0,0,1,0,0,0,0]
        for i in range(0,len(p)):
            if p[i]==1:
                print("* ",end="")
            else:
                print("  ",end="")
            if i==4 or i==9 or i==14 or i==19:
                print()
    elif word=='R':
        R=[1,1,1,1,1, 1,0,0,0,1,1,1,1,1,1,1,1,1,0,0, 1,0,0,1,1]
        for i in range(0,len(R)):
            if R[i]==1:
                print("* ",end="")
            else:
                print("  ",end="")
            if i==4 or i==9 or i==14 or i==19:
                print()

    elif word=='A':
        A=[0,0,1,0,0,0,1,0,1,0,1,1,1,1,1,1,0,0,0,1,1,0,0,0,1]
        for i in range(0,len(A)):
            if A[i]==1:
                print("* ",end="")
            else:
                print("  ",end="")
            if i==4 or i==9 or i==14 or i==19:
                print()
    elif word=='C':
        C=[0,1,1,1,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,1,1,1]
        for i in range(0,len(C)):
            if C[i]==1:
                print("* ",end="")
            else:
                print("  ",end="")
            if i==4 or i==9 or i==14 or i==19:
                print()
    elif word=='H':
        H=[1,0,0,0,1,1,0,0,0,1,1,1,1,1,1,1,0,0,0,1,1,0,0,0,1]
        for i in range(0,len(H)):
            if H[i]==1:
                print("* ",end="")
            else:
                print("  ",end="")
            if i==4 or i==9 or i==14 or i==19:
                print()

    elif word=='I':
        I=[1,1,1,1,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,1,1,1,1]
        for i in range(0,len(I)):
            if I[i]==1:
                print("* ",end="")
            else:
                print("  ",end="")
            if i==4 or i==9 or i==14 or i==19:
                print()
    else :
        print("Sorry you have entered wrong character")