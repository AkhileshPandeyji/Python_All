#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[6]:


x = np.array([i for i in range(0,10)])


# In[7]:


print(x)


# In[9]:


y = np.array(x)


# In[10]:


y = np.array([1,2,3,10.5])


# In[11]:


print(y)


# In[12]:


y1 = np.array([1,2.3,4.5,"hello"])


# In[13]:


print(y1)


# In[14]:


y1.shape #order


# In[15]:


y1.ndim #n no of dimensions


# In[16]:


print(y1[0:2]) #slicing


# In[18]:


x1 = np.array([[1,2,4],[3,4,6],[8,9,0]])


# In[19]:


print(x1)


# In[20]:


x1.shape


# In[21]:


x1.ndim


# In[22]:


print(x1[0:2])


# In[24]:


print(x1[0:2][0:1])


# In[26]:


print(x1[0:2,0:2]) #x[row][col] slicing


# In[27]:


#x3 =[]
#for i in range(0,10):
    #x3.append(i)
x3 = np.array([i for i in range(0,10)])


# In[28]:


x4 = x1.reshape(1,9)


# In[29]:


print(x4)


# In[30]:


x5 = x4.T


# In[31]:


print(x5)


# In[32]:


x5.flatten()


# In[34]:


#first method 
#np.array()
#second method
np.zeros(5)


# In[36]:


np.zeros((5,5))


# In[37]:


np.ones(5)


# In[38]:


np.ones((5,5))


# In[39]:


np.identity(5)


# In[41]:


np.identity(5)


# In[46]:


np.linspace(1,10,)


# In[47]:


np.linspace(1,10,num=10,retstep=True)


# In[51]:


#ravi4all


# In[3]:


np.random.random() #0-1 random number


# In[4]:


np.random.random(size=(2,2))#returns 2x2 array of random numbers b/w 0-1


# In[5]:


np.random.randint(5,50,10)#returns 10 random numbers b/w 5-50


# In[6]:


np.random.randn(5,5) #returns any random floats of 5x5 order array


# In[10]:


np.random.seed(0)


# In[12]:


np.random.randint(5,50,10)


# In[23]:


#numpy methods
arr = np.random.randint(1,100,100)


# In[16]:


arr.min()


# In[17]:


arr.max()


# In[18]:


arr.argmin()


# In[19]:


arr.argmax()


# In[24]:


arr.argsort()


# In[25]:


arr.sort()


# In[26]:


arr.argsort()


# In[27]:


arr.mean()


# In[28]:


#seventh method of creating arrays
np.arange(1,100,10)
#generates 1-D array from start


# In[ ]:




