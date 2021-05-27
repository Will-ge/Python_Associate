# -*- coding: utf-8 -*-
"""
Created on Thu May 27 12:46:04 2021

@author: jinji
"""

lst_input=[]
for i in range(9):
    lst_input+=[input('plz input a row:')]

# row check
def row_check(lst_input):
    for i in lst_input:
        # repeat check
        for j in range(1,10):
            if i.find(str(i))==-1:
                return "No"
        for j in i:
            # range check
            if int(j) not in range(1,10):
                return "No"
            
    return("Yes")

def column_check(lst_input):
    for i in range(9):
        column=""
        for j in lst_input:
            '''
            # range check, done also in row_check
            if int(j[i]) not in range(10):
                return "No"
            '''
            column+=j[i]
        # repeat check
        for i in range(1,10):
            if column.count(str(i))!=1:
                return "No"
            
    return "Yes"

def final_check(lst_input):
    if row_check(lst_input)==column_check(lst_input)=='Yes':
        return 'Yes'
    return 'No'
    
print(final_check(lst_input))
    
    
    
    
    