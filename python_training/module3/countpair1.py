from array import array
def getPairsCount(arr, n, sum):
    count = 0
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == sum:
                print(arr[i],arr[j])
                count += 1

    return count
arr = array('i',[1, 5, 2, 4])
n = len(arr)
sum = 6
print("Count of pairs is",getPairsCount(arr, n, sum))