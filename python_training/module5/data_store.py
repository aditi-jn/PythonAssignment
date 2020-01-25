datastore={'office':{'medical':[
    {'room_number':100,'use':'reception','sq_ft':50,'price':75},
    {'room_number': 101, 'use': 'waiting', 'sq_ft': 250, 'price': 75},
    {'room_number': 102, 'use': 'examination', 'sq_ft': 125, 'price': 150},
    {'room_number': 103, 'use': 'examination', 'sq_ft': 125, 'price': 150},
    {'room_number': 104, 'use': 'office', 'sq_ft': 150, 'price': 100},],
    "parking":{'location':'premium','style':'covered','price':750}}}

def change_roomno(datastore):
    room=int(input("Enter Room Number :"))
    new_room=int(input("Enetr New room number :"))
    for i in range(0,3):
        for j in range(0,5):
            if room==datastore['office']['medical'][j]['room_number']:
                datastore['office']['medical'][j]['room_number']=new_room

    print(datastore)

def change_prize(datastore):
    room=int(input("Enter Room Number :"))
    prize=int(input("Enetr prize :"))
    for i in range(0,3):
        for j in range(0,5):
            if room==datastore['office']['medical'][j]['room_number']:

                datastore['office']['medical'][j]['price']=prize

    print(datastore)

def del_room(datastore):
    room=input("Enter room number :")
    room=int(room)
    for i in range(0,5):
        if room==datastore['office']['medical'][i]['room_number']:
            del datastore['office']['medical'][i]['room_number']
            del datastore['office']['medical'][i]['use']
            del datastore['office']['medical'][i]['sq_ft']
            del datastore['office']['medical'][i]['price']
    print(datastore)

def add_data(datastore):
    rno=int(input("Enter room number :"))
    us= input("Enter use :")
    sq = int(input("Enter square feet:"))
    pri= int(input("Enter price :"))
    d={'room_no':rno,'use':us,'sq_ft':sq,'price':pri}
    datastore['office']['medical'].append(d)
    print(datastore)

num=int(input("Enter 1 for change roomno\n 2 for change prize\3 3 for delete room\n 4 for add data :")
if num==1:
    change_roomno(datastore)
elif num==2:
    change_prize(datastore)
elif num==3:
    del_room(datastore)
elif num==4:
    add_data(datastore)
else:
    print("Sorry dear! you have entered wrong number:")