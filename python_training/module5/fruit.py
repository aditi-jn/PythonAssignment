fruit={'Fruit':{'Name':['Apple','Mango','Banana'],
       'bionomical_value':['maius_domestica','mangi_fera_indica','musa'],
       'major_producer':[['China','US','Turky'],['India','China','Maghalay'],['Austrila','Nepal','Bhutan']],
       'Nutrition':{'Carbohydrate':['13.81','12.2','123'],'Protein':['54','54','53'],'Fats':['23','35','41']}}}
print(fruit)
c=[]
for i in range(0,3):
    if fruit['Fruit']['Nutrition']['Protein'][i]==max(fruit['Fruit']['Nutrition']['Protein']):
        x=fruit['Fruit']['Name'][i]
print(x)