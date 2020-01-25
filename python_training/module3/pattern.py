rows=int(input("Enter number of rows :"))
for i in range(0,rows):
    for j in range(0,i):
        print("     *", end=" ")
        print("\r")
for k in range(0, rows*2):
    #for l in range(0, k*2):\
    print("*", end=" ")
print()
for i in range(0,rows):
    for j in range(0,i):
        print("     *", end=" ")
        print("\r")
