# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 11:38:17 2020

@author: Adrian Mehl

Sudoku Solver: Solves every Sudoku with a systematic approach. 
                No iterative process.

"""
import pandas as pd
import numpy as np

a = np.zeros((10, 9, 9))

#initialisierung

def initialize(a):
    a[1,:,:]=int(1)
    a[2,:,:]=int(2)
    a[3,:,:]=int(3)
    a[4,:,:]=int(4)
    a[5,:,:]=int(5)
    a[6,:,:]=int(6)
    a[7,:,:]=int(7)
    a[8,:,:]=int(8)
    a[9,:,:]=int(9)
    return a


#function check square
def check_square(x,y):
    if a[0,y,x]==0:
        #define range of square (rows)
        if x%3==0:
            startrow=x
            endrow=x+2
        elif x%3==1:
            startrow=x-1
            endrow=x+1
        elif x%3==2:
            startrow=x-2
            endrow=x
            
        #define range of square (columns)
        if y%3==0:
            startcolumn=y
            endcolumn=y+2
        elif y%3==1:
            startcolumn=y-1
            endcolumn=y+1
        elif y%3==2:
            startcolumn=y-2
            endcolumn=y
        
        #calculate...
        for row in range (startrow, endrow+1):
            for column in range (startcolumn, endcolumn+1):
                if a[0,column,row]>0:
                    a[int(a[0,column,row]),y,x]=0
        return a
            
#function check row

def check_row(x,y):
    if a[0,y,x]==0:
        for row in range (0,9):
            if a[0,y,row]>0:
                a[int(a[0,y,row]),y,x]=0
    return a

#function check column

def check_column(x,y):
    if a[0,y,x]==0:
        for column in range (0,9):
            if a [0,y,x]==0:
                if a[0,column,x]>0:
                    a[int(a[0,column,x]),y,x]=0
    return a
            
#clean fields with already a number written in

def clean_fields(x,y):
    if a[0,y,x]>0:
        a[1:,y,x]=0
    return a

    
#check, if there is one single solution

def check_solution(x,y):
    #first: if only one solution for a field possible -> add this solution to the field
    if (np.sum(a[1:,y,x] > 0)) == 1:       
        a[0,y,x]=a[1:,y,x].sum()
    #second: If a possible solution of a field is not possible for any other field within the same row, column or quadrant -> take this solution for the field
    #define range of quadrant (rows)
    if x%3==0:
        startrow=x
        endrow=x+2
    elif x%3==1:
        startrow=x-1
        endrow=x+1
    elif x%3==2:
        startrow=x-2
        endrow=x
        
    #define range of quadrant (columns)
    if y%3==0:
        startcolumn=y
        endcolumn=y+2
    elif y%3==1:
        startcolumn=y-1
        endcolumn=y+1
    elif y%3==2:
        startcolumn=y-2
        endcolumn=y
        
    for i in range (1,10):
        if a[i,y,x]>0:
            if a[i,startcolumn:endcolumn+1,startrow:endrow+1].sum()==i or a[i,:,x].sum()==i or a[i,y,:].sum()==i:
                a[0,y,x]=i
    return a
        
if __name__ == "__main__":
    
    a = np.zeros((10, 9, 9))
    
    #enter Sudoku
    
    a[0,0,0]=1
    a[0,0,3]=5
    a[0,0,4]=7
    a[0,0,6]=3
    
    a[0,1,6]=5
    a[0,1,7]=7
    
    a[0,2,0]=6
    a[0,2,4]=9
    a[0,2,8]=8
    
    a[0,3,7]=4
    a[0,3,8]=1
    
    a[0,4,3]=6
    a[0,4,5]=3
    
    a[0,5,0]=7
    a[0,5,1]=2
    a[0,5,2]=8
    
    a[0,6,1]=9
    a[0,6,3]=2
    a[0,6,5]=6
    
    a[0,7,5]=1
    a[0,7,6]=2
    a[0,7,8]=3
    
    a[0,8,0]=3
    a[0,8,1]=5
    a[0,8,2]=2
    a[0,8,6]=9
    
    
    #initialize       
    initialize (a)        
           
    while a[1:,:,:].sum()>0:
        
        #clean fields
        for x in range (0,9):
            for y in range (0,9):
                clean_fields(x,y)
              
        #check solutions
        for x in range (0,9):
            for y in range (0,9):
                check_solution(x,y)
                for x2 in range (0,9):
                    for y2 in range (0,9):
                        check_square(x2,y2)
                        check_row(x2,y2)
                        check_column(x2,y2)


    print(a[0,:,:])
        
