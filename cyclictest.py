# coding=gbk

temps = ["a", "b", "c"]
for tes in temps:
    print("for循环a-b:" + tes)

# In[26]:

i = 0
while i < 3:
    i += 1
    print(i)

# In[27]:

for i in range(2):
    print(i)

# In[33]:

temps = [["a", "b", "c"], ["a1", "b1", "c1"]]
print(temps)
for te in temps:
    print(te)
for i in temps:
    for j in i:
        print(j)
