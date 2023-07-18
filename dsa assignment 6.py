#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Question 1


# In[ ]:


def perm(s):
    minn=0
    maxn=len(s)
    ans=[]
    for i in s:
        if i=="I":
            ans.append(minn)
            minn+=1
        else:
            ans.append(maxn)
            maxn-=1
    if s[-1] == "I":
        ans.append(minn)
    else:
        ans.append(maxn)
    return ans
s = "IDID"
print(perm(s))


# In[ ]:


Question 2


# In[10]:


def search2d(arr,target):
    l,r=0,len(arr[0])-1
    top,bottom=0,len(arr)-1
    while(top<=bottom):
        mid=(top+bottom)//2
        if target<arr[mid][0]:
            bottom=mid-1
        elif(target>arr[mid][-1]):
            top=mid+1
        else:
            break
    mid=(top+bottom)//2
     
    while(l<=r):
        col=(l+r)//2
        if (target>arr[mid][col]):
            l=col+1
        elif(target<arr[mid][col]):
            r=col-1
        else:
            return True
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 8
print(search2d(matrix,target))


# In[ ]:


Question 3


# In[22]:


def mountain(arr):
    i=len(arr)
    if(i<3):
        return False
    i=0
    while(i<len(arr)-1):
        if (arr[i]<arr[i+1]):
            i+=1
        elif(arr[i]==arr[i+1]):
            return False
        else:
            break
    
    if (i<2):
        return False
    else:
        while(i<len(arr)-1):
            if(arr[i]<arr[i+1]):
                return False
            i+=1
        return True
arr = [0,1,2,3,4,5,6,7,3,2,1]
print(mountain(arr))


# In[ ]:


Question 4


# In[29]:


def findMaxLength(nums):
    if len(nums) == 0:
        return 0
    
    maxLen = 0
    presum = 0
    hashmap = {0: -1}
    
    for i in range(len(nums)):
        if nums[i] == 0:
            presum -= 1
        elif nums[i] == 1:
            presum += 1
        
        if presum in hashmap:
            idx = hashmap[presum]
            currLen = i - idx
            maxLen = max(maxLen, currLen)
        else:
            hashmap[presum] = i
    
    return maxLen
arr= [0,1,0,0,1,0,1,1,1]
print(findMaxLength(arr))


# In[ ]:


Question 5


# In[37]:


def productSum(arr1,arr2):
    arr1.sort(reverse=True)
    arr2.sort()
    sum=0
    i=0
    while(i<len(arr1)):
        sum+=(arr1[i]*arr2[i])
        i+=1
    return sum
nums1 = [5,3,4,2]
nums2 = [4,2,2,5]
print(productSum(nums1,nums2))


# In[ ]:


Question 6


# In[ ]:


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


Question 7


# In[ ]:


def spiral(arr):
    ans=[]
    l,r=0,len(arr[0])
    top,bottom=0,len(arr)
    while(l<r and top<bottom):
        for i in range(l,r):
            ans.append(arr[top][i])
        top+=1
        for i in range(top,bottom):
            ans.append(arr[i][r-1])
        r-=1
        if not (l<r and top<bottom):
            break
        for i in range(r-1,l-1,-1):
            ans.append(arr[bottom-1][i])
        bottom-=1
        for i in range(bottom-1,top-1):
            ans.append(arr[i][l])
        l+=1
    return ans
arr=[[0,3,4,5],[3,5,6,7],[3,5,8,8]]
print(spiral(arr))


# In[ ]:


Question 8


# In[38]:


def multiply(mat1, mat2):
    m, k = len(mat1), len(mat1[0])
    k2, n = len(mat2), len(mat2[0])

    result = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(k):
            if mat1[i][j] != 0:
                for col in range(n):
                    result[i][col] += mat1[i][j] * mat2[j][col]

    return result

mat1 = [[1,0,0],[-1,0,3]]
mat2 = [[7,0,0],[0,0,0],[0,0,1]]
print(multiply(mat1,mat2))


# In[ ]:




