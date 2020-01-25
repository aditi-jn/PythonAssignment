# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 15:28:36 2020

@author: jedaix
"""
import pickle
datastore={}

no=int(input('Enter the no of contacts you want to enter'))

class info:
    def __init__(self,name,phone,email):
        self.name=name
        self.phone=phone
        self.email=email
   
    def get_name(self,name):
        return self.name
    def get_phone(self,phone):
        return self.phone
    def get_email(self,email):
        return self.email
    def __repr__(self):
        return "%s,%s,%s"%(self.name,self.email,self.phone)
"""def add():
   for i in range(no):
       name=input('Enter your name')
       phone=input("enter your phone no")
       email=input('Enter your email')
       c=info(name,phone,email)
       datastore[i]=c
       print(datastore)
       if i==no:
           outfile=open('datastore.dat','wb')
           pickle.dump(datastore,outfile)
           outfile.close()
print(add())"""

def search():
    infile=open('datastore.dat','rb')
    print(pickle.load(infile))
    '''k=int(input('enter the key you need to search the'))
    print(d[k])'''
print(search())   
