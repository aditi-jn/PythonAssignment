#Flatter a given 2D list
''' Suppose I want to Flatten a given 2D List :
matrix=[[1,2,3],[4,5,6],[7,8,9]]
Expected Output : flatten_matrix=[1,2,3,4,5,6,7,8,9]'''

matrix2=[[1,2,3],[4,5],[6,7,8,9]]
flatten_matrix=[]
for sublist in matrix2:
    for val in sublist:
        flatten_matrix.append(val)
print(flatten_matrix)

# Optimize Way
flatt_matrix=[val for sublist in matrix2 for val in sublist]
print(flatt_matrix)