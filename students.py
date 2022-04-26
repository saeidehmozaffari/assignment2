#!/usr/bin/env python
# coding: utf-8

# In[1]:


scores=[]
sumscores=0

numberofstudents=int(input('enter numbebr of students:'))
for num in range(numberofstudents):
    score=int(input('score'))
    if 0<=score<=20:
        scores.append(score)
        sumscores+=scores[num]
    else:
        print('enter score correctly')
        break
maxscore=scores[0]
minscore=scores[0]

for i in scores:
    if i>=maxscore:
        maxscore=i
    if i<minscore:
        minscore=i
print(scores)
print('minscore is:'+str(minscore))
print('maxscore is:'+str(maxscore))
print('average is:'+str(sumscores/numberofstudents))


# In[2]:


average


# In[ ]:




