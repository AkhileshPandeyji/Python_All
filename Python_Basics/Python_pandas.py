#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pandas important
#series - 1-D
#Dataframe - 2-D
#panel


# In[2]:


import pandas as pd
import numpy as np


# In[3]:


names = ["Sachin","Yuvraj","Dhoni"]


# In[5]:


s = pd.Series(names)


# In[6]:


s


# In[7]:


s[0]


# In[9]:


scores = [100,200,None]


# In[10]:


avg = [49.57,None,39.87]


# In[12]:


dataset = {
    "names" : names,
    "scores" : scores,
    "avg" : avg

}


# In[14]:


y = pd.DataFrame(dataset)


# In[15]:


y.shape #returns the dimension of the table


# In[16]:


y.head() #returns the table of first five rows


# In[17]:


y.tail() #returns the table of last five rows


# In[18]:


y.describe()


# In[19]:


#std - standard deviation -consistency


# In[24]:


y['names'].head()


# In[27]:


y[y['scores']>40]


# In[30]:


y.isna() #returns the table of boolean values representing Nan values


# In[31]:


y.dropna() #drop those rows with Nan values


# In[39]:


y.fillna(0)


# In[40]:


#slicing in pandas


# In[42]:


y.iloc[0]


# In[43]:


y.loc[0]


# In[47]:


y.iloc[0:3,1] #iloc[row,col] slicing indexlocation


# In[48]:


y = y.fillna(0)


# In[49]:


y


# In[ ]:




