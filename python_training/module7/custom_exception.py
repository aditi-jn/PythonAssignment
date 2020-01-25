# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 12:24:01 2020

@author: jedaix
"""

class MyError(Exception):
   def __init__(self,value):
       self.value=value
   def __str__(self):
      return(repr(self.value))
      
try:
   raise(MyError(3*2))
except MyError as error:
    print('A newexception has occured',error.value)

      