import collections
list1=[1,5,2,3,1,2,3,2,1,5,1]
counter = collections.Counter(list1)
value=list(counter.values())
print("Frequrncy with elements :",counter)
print("Frequency of elements: ",value)
for i in range(0,len(value)):
    print()
