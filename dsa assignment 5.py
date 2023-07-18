#!/usr/bin/env python
# coding: utf-8

# # 1.

# In[21]:


def convert(arr, m, n):
    a = []
    ans = []
    for i in range(len(arr)):
        if len(ans) == n:
            a.append(ans)
            ans = []
        ans.append(arr[i])
    
    if ans:  # Append the remaining elements of ans if any
        a.append(ans)
    
    return a

original = [1, 2, 3,4,5,6,7,9, 4]
m = 3
n = 3
print(convert(original, m, n))


# # 2.

# In[33]:


def arrangecoin(n):
    l,r=0,n
    res=0
    while(l<=r):
        mid=(l+r)//2
        coin=(mid*(mid+1))//2
        if coin==n:
            return mid
        elif coin<n:
            l=mid+1
            res=max(res,mid)
        else:
            r=mid-1
    return res
n=10
print(arrangecoin(n))


# # 3.

# In[34]:


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


# # 4.

# In[41]:


def distinct(arr1,arr2):
    ans=[]
    arr1,arr2=set(arr1),set(arr2)
    ans.append(list(arr1-arr2))
    ans.append(list(arr2-arr1))
    return ans
arr1=[2,4,5]
arr2=[4,6,7]
print(distinct(arr1,arr2))


# # 5.

# In[39]:


def distance(arr1,arr2,d):
    arr2.sort()
    n1,n2,c=len(arr1),len(arr2),0
    for i in arr1:
        l=0
        r=n2-1
        while(l<=r):
            mid=(l+r)//2
            if(abs(i-arr2[mid])<=d):
                c+=1
                break
            if(arr2[mid]>i):
                r=mid-1
            else:
                l=mid+1
    return n1-c
    
arr1 = [4,5,8]
arr2 = [10,9,1,8]
d = 2
print(distance(arr1,arr2,d))


# # 6.

# In[44]:


def duplicates(arr):
    ans=[]
    for i in arr:
        i=abs(i)
        if(arr[i-1]>0):
            arr[i-1]*=(-1)
        else:
            ans.append(i)
    return ans
nums = [4,3,2,7,8,2,3,1]
print(duplicates(nums))


# # 7.

# In[48]:


def rotatemin(arr):
    l,r=0,len(arr)-1
    res=arr[0]
    while(l<=r):
        if arr[l]<arr[r]:
            res=min(res,arr[l])
            break
        mid=(l+r)//2
        res=min(res,arr[mid])
        if(arr[mid]>=arr[l]):
            l=mid+1
        else:
            r=mid-1
    return res

nums = [3,4,5,0,1,2]
print(rotatemin(nums))


# # 8.

# In[83]:


def findOriginalArray(changed):
    arr = {}
    ans = []
    changed.sort()
    if (len(changed)%2!=0):
        return {}
    for i in changed:
        arr[i] = 1

    for i in range(len(arr)):
        if arr.get(i) == 0:
            continue

        if arr.get(2 * i) == 0:
            return []

        if arr.get(i):
            if arr.get(2 * i):
                arr[2 * i] -= 1
                ans.append(i)
    if (len(ans)==len(changed)//2):
        return ans
    else:
        return {}
    


# In[ ]:





# In[ ]:




