list1 = [1, 2, 3, 7]
list2 = [4, 3, 2, 6]
def getPairsCount(sum):
    count = 0
    sum=5
    for i in range(0, len(list1)):
        for j in range(0, len(list2)):
            if list1[i] + list2[j] == sum:
                print(list1[i],list2[j])
                count += 1

    return count
print("Count of pairs is",getPairsCount(sum))
