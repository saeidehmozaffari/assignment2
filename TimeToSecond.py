#!/usr/bin/env python
# coding: utf-8

# In[11]:


try:
    time=input('enter time 00:00:00')
    time=time.split(':')
    second=int(time[2])
    minute=int(time[1])
    hour=int(time[0])
    if 0<=second<60 and 0<=minute<60 and 0<=hour<24:
        sum=hour*3600+minute*60+second
        print(sum,'seconds')
    else:
        print('enter correct time!')
except:
    print('enter correct time!!')


# In[ ]:




