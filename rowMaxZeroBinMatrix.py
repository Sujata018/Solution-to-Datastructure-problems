#!/usr/bin/env python
# coding: utf-8

# In[168]:


def createRandomMatrix(n):
    matrix = [createRow(n) for x in range(n)]
    return matrix


# In[169]:


from random import randint

def createRow(n):
    row = [randint(1,3)%2 for x in range(n)]
    for i in range(n):
        if row[i] == 0:
            break
    if i < n:
        row[i:] = [0]*(n-i)
    return row


# In[170]:


''' This program creates a random square 2-D binary matrix given dimension,
    such that all 0s appear after the 1s.
    It then prints the index of the row having maximum number of zeros in it
'''
n=int(input("Enter dimension of the matrix:"))
m = createRandomMatrix(n)           # create the matrix
#m=[[1,0],[0,0]]
print(m)            
print("Row index with maximum 0s:")
print(findMaxZero(m))               # find row with max 0s


# In[171]:


'''
  This program checks following path to find out the row with maximum zeros
  
  1-> 1-> 1-> 1   0
              |    
  1   1   1<- 0   0
          |
  1   1   1   1   1
          |
  1<- 0 <-0   0   0
  |
  1   1   0   0   0

  It returns 3 as the index of 4th row.
'''


def findMaxZero(m):
    row=0
    col=0
    while(m[row][col])&(col<len(m)): #Move right until a 0 is found
        print("moving right m[",row,"][",col,"]")
        col += 1
        if col == len(m):
            break
    if col ==0:
        return row                         #If first row, first column contains the 0, then that's the row with all zeros. Return it.   
    else:
        return moveDownOrLeft(m,row,col-1)   #Check down, if it is 0 then move left until a 1 is found, then move down 


# In[173]:


''' The cursor is at position (row,col) 
    if M[row][col] = 1, then move down i.e. check next row
    if M[row][col] = 0, then move left i.e. find first 0 in the row
'''

def moveDownOrLeft(M,row,col):
    
    z=0
    while (col >=0)&(row < len(M)):
        #print("at m[",row,"][",col,"]")
        if M[row][col] :
            row += 1
        else:
            z = row
            col -= 1
    return z


# In[ ]:




