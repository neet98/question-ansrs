#!/usr/bin/env python
# coding: utf-8

# ## 1. Complete the following code to find the area of an equilateral triangle. Output should be as displayed

# In[1]:


import math
side = float(input("Enter the side of the equilateral triangle: "))
area = ((math.sqrt(3))/4)*pow(side,2)
print(round(area,1))


# ## 2. Write a program to count the number of each characters in a string

# In[2]:


s=input("Enter string:")
l=[]
for k in s:
    if k in l:
        pass
    else:
        l+=[k]
for k in l:
    print("Char:",k,"No of char",s.count(k))
    


# ## 3. Write a program to find the area and perimeter of a rectangle using functions

# In[20]:


length, breadth = (input("Enter length and breadth of rectangle: ").split())
length = int(length)
breadth = int(breadth)

def area_rect(length, breadth):
    area = length * breadth
    return area

def perim_rect(length, breadth):
    perim = 2*(length + breadth)
    return perim

print("Area of rectangle: ", area_rect(length, breadth), "Perimeter of rectangle: ", perim_rect(length, breadth))


# ## 4. Write a program to print the fibonacci series till a specified number

# In[24]:


num = int(input("Enter the Number:"))
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")

print()


# ## 5. Complete the following code to find the minimum of 3 number using conditional statements. Output should be as displayed

# In[29]:


a,b,c = input("Enter three numbers followed by  : ").split()
a= int(a)
b=int(b)
c=int(c)
print("First number :",a)
print("Second number :",b)
print("Third number :",c)

if(a==b==c):
    print("Entered numbers are equal!!!")
elif(a<b and a<c):
    print(a," is smallest")
elif(b<a and b<c):
    print(b," is smallest")
elif(c<a and c<b): 
    print(c," is smallest")


# ## 6. Write a program to print star pyramind. The number of rows should be taken as input from the user

# In[6]:


rows =int(input("Enter the number of rows: "))
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*",end='')
    print(" ")


# ## 7. Complete the following code to convert hour into seconds. Output should be as displayed

# In[10]:


def to_seconds(t):
    t = t *60 *60
    return t

time_in_hours = int(input("Enter time in hours"))
print(time_in_hours ," Hour is equal to" ,to_seconds(time_in_hours) ," Seconds")


# ## 8. Write a program to print multiplication table as below

# In[13]:


num = int(input('Enter a number to find the multiplication table:'))
for i in range(1, 11):
    print(i,"X", num, "=", (i*num))
    


# ## 9. Write a program to take your 5 favorite food as list and print each as 'I like Biriyani'

# In[19]:


fav_food = input('Enter your 5 favorite food :')
fav_food = fav_food.split(" ")
for i in range(len(fav_food)):
    print("I like", fav_food[i])


# In[ ]:





# In[ ]:




