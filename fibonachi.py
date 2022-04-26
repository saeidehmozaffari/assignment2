#!/usr/bin/env python
# coding: utf-8

# In[5]:


n=int(input('enter a number:'))
if n==0:
    print(0)
elif n==1:
    print(1)
else:
    serifibonachi=[0,1]
    for i in range(1,n):
        serifibonachi.append((serifibonachi[i-1])+serifibonachi[i])
print(serifibonachi)
    


# In[ ]:




