#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("ddddddddddddd")


# In[7]:


print(8**2)


# In[3]:


#LIST
months = []
months.append("test1")
months.append("test2")
print(months)


# In[6]:


#LIST
months = []
print(months)
months.append(1)
months.append("test1")
months.append("test2")
months.append(2)
print(months)
print(type(months))


# In[8]:


temps = ["China", 122.5, "India",55]


# In[11]:


test1 = []
test2 = []
test1.append("a")
test1.append("b")
test1.append("c")
test2.append(1)
test2.append(2)
test2.append(3)
print(test1)
print(test2)
print(test1[1])
print(test2[1])
print(len(test2))
# print(test2[3])


# In[20]:


temps = ["China", 122.5, "India",55]
print(temps[-2])
print(temps[1:3])
print(temps[1:])
print(temps[:1])
print(temps[:-1])


# In[29]:


temps = ["a", "b", "c"]
for tes in temps:
    print(tes)


# In[26]:


i = 0
while i < 3:
    i += 1
    print(i)


# In[27]:


for i in range(10):
    print(i)


# In[33]:


temps = [["a", "b", "c"],["a1", "b1", "c1"]]
print(temps)
for te in temps:
    print(te)
for i in temps:
    for j in i:
        print(j)


# In[ ]:




