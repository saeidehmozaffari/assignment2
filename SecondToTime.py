#!/usr/bin/env python
# coding: utf-8

# In[25]:



time=int(input('enter seconds'))
hour=time/3600
time=time%3600
minute=time/60

second=time%60
print(round(hour),':',round(minute),':',second)


# In[ ]:




