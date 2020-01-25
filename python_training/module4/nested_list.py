#Nested list comprehension
matrix=[]
for i in range(5):
    #Append an empty sublist inside the list
    matrix.append([])
    for j in range(5):
        matrix[i].append(j)
print(matrix)
# Optimizes way
matrix1=[[j for j in range(5)] for i in range(5)]
print(matrix1)

