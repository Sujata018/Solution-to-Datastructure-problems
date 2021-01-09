#!/usr/bin/env python
# coding: utf-8

# In[36]:


def mergesort(A,start,end):
    if start < end:            # length of sub array is 1
        mid = (start+end)//2
        mergesort(A,start,mid)
        mergesort(A,mid+1,end)
        merge(A,start,mid,end)
    return      


# In[37]:


def merge(A,start,mid,end):
    i=j=0                                  # indexes of front elements of subarrays to be merged
    k=start                                # index of original array A where elements are placed after merging 
    A1 = [_ for _ in A[start:mid+1]]       # copy start to mid elements to a different array
    A2 = [_ for _ in A[mid+1:end+1]]       # copy mid to end elements to a different array
    while ((i<mid-start+1) & (j<end-mid)): # merge both arrays and place in the original array A
        if A1[i] < A2[j]:
            A[k] = A1[i]
            i +=1
        else:
            A[k]=A2[j]
            j += 1
        k +=1

    while i< mid-start+1:
        A[k] = A1[i]
        i += 1
        k += 1
    
    while j<end-mid:
        A[k] = A2[j]
        j += 1
        k += 1
     
    return 


# In[38]:


'''
Compares expected output with actual output.
If matched, prints 'ok', or else prints the actual output
'''
def test(A,B):             
    n=len(A)
    mergesort(A,0,n-1)
    if A==B:
        print("ok!")
    else:
        print("Test case failed:",A)


# In[39]:


test([3,1,6,3,2,8],[1,2,3,3,6,8])
test(['F','R','Frog','Elephant','Rat'],['Elephant','F','Frog','R','Rat'])

