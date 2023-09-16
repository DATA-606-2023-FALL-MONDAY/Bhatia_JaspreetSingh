#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


ds= pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")
ds.head()


# In[8]:


ds.tail()


# In[4]:


ds.shape


# In[7]:


ds.columns


# In[10]:


ds.dtypes


# In[13]:


ds.info()


# In[15]:


ds.isnull().sum()


# In[16]:


set(ds['gender'])


# In[17]:


set(ds['SeniorCitizen'])


# In[18]:


set(ds['tenure'])


# In[26]:


set(ds['InternetService'])


# In[24]:


set(ds['MultipleLines'])


# In[22]:


set(ds['OnlineSecurity'])


# In[23]:


set(ds['DeviceProtection']) 


# In[27]:


set(ds['TechSupport'])        


# In[29]:


set(ds['StreamingMovies'])  


# In[30]:


set(ds['Contract'])              


# In[31]:


set(ds['PaperlessBilling'])                


# In[32]:


set(ds['PaymentMethod'])                       


# In[43]:


max(set(ds['MonthlyCharges']))


# In[41]:


set(ds['TotalCharges'])


# In[47]:


set(ds['Churn'])


# In[ ]:




