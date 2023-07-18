#!/usr/bin/env python
# coding: utf-8

# # 1.

# In[12]:


def find(arr1,arr2,arr3):
    l1,l2,l3,r1,r2,r3=0,0,0,len(arr1),len(arr2),len(arr3)
    ans=[]
    while(l1<r1 and l2<r2 and l3<r3):
        if (arr1[l1]==arr2[l2]==arr3[l3]):
            ans.append(arr1[l1])
            l1+=1
            l2+=1
            l3+=1
        elif(arr1[l1]<arr2[l2] ):
            l1+=1
        elif(arr2[l2]<arr3[l3] ):
            l2+=1
        else:
            l3+=1
    return ans
arr1=[2,3,4,5,6]
arr2=[3,4,6,8,9]
arr3=[4,6,7,8,9]
print(find(arr1,arr2,arr3))


# # 2.

# In[13]:


def distinct(arr1,arr2):
    ans=[]
    arr1,arr2=set(arr1),set(arr2)
    ans.append(list(arr1-arr2))
    ans.append(list(arr2-arr1))
    return ans
arr1=[2,4,5]
arr2=[4,6,7]
print(distinct(arr1,arr2))


# # 3.

# In[14]:


def transpose(arr):
    for i in range(1,len(arr)):
        for j in range(i+1):
            arr[i][j],arr[j][i]=arr[j][i],arr[i][j]
    return arr
arr=[[2,4,-1],[-10,5,11],[18,-7,6]]
print(transpose(arr))


# # 4.

# In[19]:


def maximized(arr):
    arr.sort()
    ans=0
    for i in arr[::2]:
        ans+=i
    return ans
nums = [1,4,3,2]
print(maximized(nums))


# # 5.

# In[28]:


def arrangecoin(n):
    l,r=0,n
    while(l<r):
        mid=(l+r)//2
        coin=(mid*(mid+1))//2
        if(coin==n):
            return mid
        elif(coin<n):
            l=mid+1
        else:
            r=mid-1
    return l
n=6
print(arrangecoin(n))


# # 6.

# In[41]:


def squares(arr):
    ans=[]
    l,r=0,len(arr)-1
    while(l<=r):
        if(arr[l]**2<arr[r]**2):
            ans.append(arr[r]**2)
            r-=1
        else:
            ans.append(arr[l]**2)
            l+=1
    ans.sort()
    return ans
arr=[-4,-1,0,3,10]
print(squares(arr))


# # 7.

# In[1]:


def maxCount(m,n,ops) :
    if not ops : return m * n
    lmin, rmin = ops[0]
    for x, y in ops :
        if x < lmin : lmin = x
        if y < rmin : rmin = y

    return lmin * rmin
m = 3
n = 3
ops = [[2,2],[3,3]]
print(maxCount(m,n,ops))


# # 8.

# In[3]:


def shuffle(arr,n):
    for i in range(n):
        arr[i]=arr[i]<<10
        arr[i]=arr[i] | arr[i+n]
    j=2*n-1
    for i in range(n-1,-1,-1):
        y=arr[i] & (2**10 -1)
        x=arr[i] >> 10
        
        arr[j]=y
        arr[j-1]=x
        j-=2
    return arr

arr= [2,5,1,3,4,7]
n=3
print(shuffle(arr,n))


# In[ ]:




