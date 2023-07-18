#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1. Given two strings s and t, *determine if they are isomorphic*.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.


# In[3]:


def isomorphic(str1,str2):
    if(len(str1)!=len(str2)):
        return False
    ST,TS={},{}
    for i in range(len(str1)):
        c1,c2=str1[i],str2[i]
        if ((c1 in ST and ST[c1]!=c2) or (c2 in TS and TS[c2]!=c1)):
             return False
        ST[c1]=c2
        TS[c2]=c1
            
    return True
s = "egg"
t = "ddd"
print(isomorphic(s,t))


# In[ ]:


Given a string num which represents an integer, return true *if* num *is a **strobogrammatic number***.

A **strobogrammatic number** is a number that looks the same when rotated 180 degrees (looked at upside down).


# In[4]:


def is_strobogrammatic(num):
    pairs = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
    left, right = 0, len(num) - 1
    
    while left <= right:
        if num[left] not in pairs or num[right] not in pairs or pairs[num[left]] != num[right]:
            return False
        left += 1
        right -= 1
    
    return True

num = "69"
print(is_strobogrammatic(num))


# In[ ]:


Given two non-negative integers, num1 and num2 represented as string, return *the sum of* num1 *and* num2 *as a string*.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.


# In[5]:


def add_strings(num1, num2):
    result = ""
    i = len(num1) - 1
    j = len(num2) - 1
    carry = 0
    
    while i >= 0 or j >= 0 or carry != 0:
        if i >= 0:
            carry += int(num1[i])
            i -= 1
        if j >= 0:
            carry += int(num2[j])
            j -= 1
        result = str(carry % 10) + result
        carry //= 10
    
    return result

num1 = "11"
num2 = "123"
print(add_strings(num1, num2))


# In[ ]:


Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.


# In[6]:


def reverse_words(s):
    words = s.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

s = "Let's take LeetCode contest"
reverse_words(s)


# In[ ]:


Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.


# In[7]:


def reverse_str(s, k):
    s = list(s)
    for i in range(0, len(s), 2*k):
        s[i:i+k] = reversed(s[i:i+k])
    return ''.join(s)
s = "abcdefg"
k = 2
print(reverse_str(s, k))


# In[ ]:


Given two strings s and goal, return true *if and only if* s *can become* goal *after some number of **shifts** on* s.

A **shift** on s consists of moving the leftmost character of s to the rightmost position.


# In[12]:


def can_shift( A, B):
        
    if len(A) != len(B):
        return False
        
    if A == B and len(set(A)) < len(A):
        return True
    differences = []
    for x in range(len(B)):
        if A[x] != B[x]:
            differences.append([A[x], B[x]])

    if len(differences) == 2 and differences[0] == differences[-1][::-1]:
        return True
        
    return False
s = "ab"
goal = "ab"
print(can_shift(s, goal))


# In[ ]:


Given two strings s and t, return true *if they are equal when both are typed into empty text editors*. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.


# In[16]:


def backspaceCompare(s,t):
    temp=[]
    temp1=[]
    if len(s)!=0 and len(t)!=0:
        for i in s:
            if i=='#' and len(temp)!=0:
                temp.pop()
            elif i=='#' and len(temp)==0:
                pass
            else:
                temp.append(i)
        for j in t:
            if j=='#'and len(temp1)!=0:
                temp1.pop()
            elif j=='#' and len(temp1)==0:
                pass
            else:
                temp1.append(j)
        return (temp==temp1)
s = "abb#c"
t = "ad#c"
print(backspaceCompare(s,t))


# In[ ]:


You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.


# In[17]:


def checkStraightLine(coordinates):
    if len(coordinates) == 2:
        return True
    x0, x1 = coordinates[0][0], coordinates[1][0]
    y0, y1 = coordinates[0][1], coordinates[1][1]
    dx = x1 - x0
    dy = y1 - y0
    for i in range(2, len(coordinates)):
        x = coordinates[i][0]
        y = coordinates[i][1]
        if dy * (x - x0) != dx * (y - y0):
            return False
    return True

coordinates = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6,7]]
print("true" if checkStraightLine(coordinates) else "false")


# In[ ]:




