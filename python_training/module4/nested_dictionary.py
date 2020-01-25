people={1:{'Name':'John','Age':'27','Sex':'Male'},2:{'Name':'Marie','Age':'22','Sex':'Female'}}
print(people)
print(people[1]['Name'])
print(people[1]['Age'])
print(people[1]['Sex'])
#Add Element to Nested Dictionary
people[3]={}
people[3]['Name']='Luna'
people[3]['Age']='24'
people[3]['Sex']='Female'
people[3]['Married']='No'
print(people[3])
print(people)

people[4]={'Name':'Peter','Age':'29','Sex':'Male','Married':'Yes'}
print(people[4])

#Delete Elementsfrom a nested dictionary

del people[3]['Married']
del people[4]['Married']
print(people[3])
print(people[4])

# How to delete dictionary from a nested dictionary
people={1: {'Name': 'John', 'Age': '27', 'Sex': 'Male'},
        2: {'Name': 'Marie', 'Age': '22', 'Sex': 'Female'},
        3: {'Name': 'Luna', 'Age': '24', 'Sex': 'Female'},
       4: {'Name': 'Peter', 'Age': '29', 'Sex': 'Male'}}

del people[3]
del people[4]
print(people)

#Iterating through a nested dictionary
people={1: {'Name': 'John', 'Age': '27', 'Sex': 'Male'},
        2: {'Name': 'Marie', 'Age': '22', 'Sex': 'Female'}}
for p_id,p_info in people.items():
    print("\nPerson ID:",p_id)
    for key in p_info:
        print(key,'.',p_info[key])

#Nested list comprehension
matrix=[]
for i in range(5):
    #Append an empty sublist inside the list
    matrix.append([])
    for j in range(5):
        matrix[i].append(j)
print(matrix)
# Optimizes way
matrix=[[j for j in range(5)] for i in range(5)]