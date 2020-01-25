# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 11:47:20 2020

@author: jedaix
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 14:11:36 2020

@author: jedaix
"""
import pickle
datastore={'office':{'medical':[
          {'room-number':100,'use':'reception','sqt-ft':50,'price':75}
         ,{'room-number':101,'use':'waiting','sqt-ft':250,'price':75}
         ,{'room-number':102,'use':'exmaniation','sqt-ft':125,'price':150}
         ,{'room-number':103,'use':'examination','sqt-ft':125,'price':150}
         ,{'room-number':104,'use':'office','sqt-ft':150,'price':100}]
         ,'parking':{'location':'premium','style':'covered','price':750}
          }}
#print(datastore)

outfile=open('datastore.dat','wb')
pickle.dump(datastore,outfile)
outfile.close()
def change_roomnop(datastore):
   try:
      change=int(input("Enter the room no you want to change the price"))
      price=int(input("enter the price you want to give"))

   except ValueError:
      print('Enter the correct roon no and price')
      change_roomnop(datastore)
   count=0
   for i in range(0,3):
      for j in range(0,5):
          if change==datastore['office']['medical'][j]['room-number']:
             datastore['office']['medical'][j]['price']=price
             
          """else:
              count=count+1
      if count>5:
         print('enter roomno again')
         change_roomnop(datastore)"""
                    
   print(datastore)


def change_roomno(datastore):
    try:
       change=int(input("Enter the room no you want to change no"))
       nr=int(input("enter the new room no"))
    except ValueError:
        print('Enter the correct roon no and price')
        change_roomno(datastore)

    for i in range(0,3):
        for j in range(0,5):
            if change==datastore['office']['medical'][j]['room-number']:
                datastore['office']['medical'][j]['room-number']=nr
    print(datastore)

def del_room(datastore):
    try:
       change=int(input("enter the room no you want to delete the room"))
    except ValueError:
        print('Enter the correct roon no and price')
        del_room(datastore)

    for i in range(0,5):
        if change==datastore['office']['medical'][i]['room-number']:
            del datastore['office']['medical'][i]
            break
    print(datastore)

def add_room(datastore):
   try:
      room_number=int(input("enter the room no you want to add"))
      use=input("enter reception or waiting or examination or office")
      sqt_ft=int(input("enter the square feet of room"))
      
      price=int(input("Enter the price of room"))
   except:
       print('Enter the correct roon no and price')
       add_room(datastore)

   d={'room-number':room_number,'use':use,'sqt-ft':sqt_ft,'price':price}
   datastore['office']['medical'].append(d)
   print(datastore)
   
Input=input("Do you want to change price of the room enter yes or no")
if Input=='yes' or Input=='Yes' or Input=='YES':
    change_roomnop(datastore)
Input=input("Do you want to change roono of the room enter yes or no")
if Input=='yes' or Input=='Yes' or Input=='YES':
    change_roomno(datastore)
Input=input("Do you want to delete the room enter yes or no")
if Input=='yes' or Input=='Yes' or Input=='YES':
    del_room(datastore)
Input=input("Do you want to add the room enter yes or no")
if Input=='yes' or Input=='Yes' or Input=='YES':
    add_room(datastore)

    