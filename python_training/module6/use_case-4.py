# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 13:56:54 2020

@author: Student
"""

datastore={"office":{"medical":[{"room-number":100,"use":"reception","sq-ft":50,"price":75},{"room-number":101,"use":"waiting","sq-ft":250,"price":75},
                                {"room-number":102,"use":"examination","sq-ft":125,"price":150},{"room-number":103,"use":"examination","sq-ft":125,"price":150},
                                {"room-number":104,"use":"office","sq-ft":150,"price":100}],"Parking":{"location":"premium","style":"covered","price":750 }}}

def chamount(datastore):
    a=input("Enter amount to be changed:")
    r=int(input("Enter room number:"))
    for x in range(0,5):
        if r==datastore["office"]["medical"][x]["room-number"]:
          datastore["office"]["medical"][x]["price"]=a
          break
    print(datastore)    

def delrm(datastore):
    r=int(input("Enter room number:"))
    for x in range(0,5):
        if r==datastore["office"]["medical"][x]["room-number"]:
          del datastore["office"]["medical"][x]
          break
    print(datastore)
  

def adroom(datastore):
    r=int(input("Enter room number:"))
    u=input("Enter reception:")
    s=input("Enter size:")
    p=input("Enter price:")
    datastore["office"]["medical"].append([{"room-number":r,"use":u,"sq-ft":s,"price":p}])
    print(datastore)

