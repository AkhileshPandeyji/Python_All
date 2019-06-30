#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[2]:


import numpy as np


# In[13]:


x = np.arange(10,100,10)


# In[11]:


y = np.arange(10,100,10)


# In[14]:


plt.plot(x,y)


# In[15]:


plt.scatter(x,y)


# In[16]:


plt.plot(x,y,'ro')


# In[18]:


plt.plot(x,y,marker='+')


# In[19]:


plt.scatter(x,y,marker="+")


# In[20]:


parties = ['BJP','CONG','AAP','TMC']
votes = [350,50,3,32]


# In[50]:


plt.pie(votes,labels=parties,colors=['r','g','c','y'],counterclock=False,explode=[0,0.3,0,0],autopct='%1.2f%%',shadow=True,startangle=90)
plt.legend(loc=0)
plt.title('Parties vote share')
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('img-2.png')
plt.show()


# In[37]:


from matplotlib import style
style.use('ggplot')


# In[38]:


plt.plot(parties,votes)


# In[39]:


style.use("fivethirtyeight")
plt.plot(parties,votes)


# In[48]:


plt.figure(figsize=(8,6))
plt.plot(parties,votes)
plt.savefig('img-1.png')


# <h1>Complete</h1>

# In[57]:


ages = np.random.randint(1,100,40)


# In[63]:


plt.figure(figsize=(8,6))
plt.hist(ages,rwidth=0.9)


# In[64]:


gender = np.random.randint(0,2,20)


# In[67]:


plt.xlim(0,1)
plt.bar(gender,ages,align='center')


# In[ ]:




