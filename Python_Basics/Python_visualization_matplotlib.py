#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 


# In[3]:


#matches = pd.read_csv("ipl/matches.csv")
#matches.shape


# In[4]:


#matches.head()
#matches[matches["player_of_match" = "MS Dhoni"]]


# In[5]:


#matches[(matches["player_of_match" = "MS Dhoni"]) & (matches["win_by_wickets"]>3)]


# In[6]:


#pd.value_counts(matches["winner"]) returns the frequency of matches_win of particular column


# In[7]:


#matches.drop_duplicates('season',keep='last')[['season','winner']]


# In[8]:


#deliveries = pd.read_csv("ipl/deliveries.csv")


# In[9]:


#deliveries.shape


# In[10]:


#deliveries.head()


# In[11]:


#six_data = deliveries[deliveries['batsman_runs'] == 6]
#pd.value_counts(six_data['batsman']).head(10)


# In[12]:


x = np.arange(1,100,10)


# In[13]:


len(x)


# In[14]:


y = x**2


# In[15]:


plt.plot(x,y) #line plot


# In[16]:


plt.show()


# In[17]:


plt.plot(x,y,'o') #scatter plot


# In[18]:


x = np.random.randint(-1,90,10)


# In[19]:


y = np.random.randint(-9,80,10)


# In[20]:


plt.plot(x,y)


# In[21]:


plt.plot(x,y,'o')


# In[22]:


x = [23,45,15,15]
labels = ['AAP','BJP','RJD','CONG']


# In[23]:


plt.pie(x,labels=labels)


# In[24]:


plt.show()


# In[25]:


plt.pie(x,labels=labels,shadow=True)


# In[ ]:




