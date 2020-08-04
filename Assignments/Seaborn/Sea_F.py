#!/usr/bin/env python
# coding: utf-8

# In[14]:


import csv
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="darkgrid")


# In[15]:


data_T = pd.read_csv('/Users/bhanuchanderkureti/Bhanu/ITMD_513/Assignments/Seaborn/titanic.csv')
data_W = pd.read_csv('/Users/bhanuchanderkureti/Bhanu/ITMD_513/Assignments/Seaborn/workerstips.csv')
data_F = pd.read_csv('/Users/bhanuchanderkureti/Bhanu/ITMD_513/Assignments/Seaborn/flightsData.csv')
df_T= pd.DataFrame(data_T)
df_W= pd.DataFrame(data_W)
df_F= pd.DataFrame(data_F)


# In[22]:


sns.relplot(x="total_bill", y="tip", data=df_W)


# In[32]:


sns.scatterplot(x="total_bill", y="tip", hue="smoker",style ="smoker", size="size", sizes=(10, 300),legend="full", data=df_W)


# In[26]:


sns.catplot(x="day", y="tip", kind="bar", data = df_W)


# In[34]:


sns.scatterplot(x="total_bill", y="tip", hue="time",style ="time", size="size", sizes=(10, 300),legend="full", data=df_W)


# In[33]:


sns.lineplot(x="year", y="passengers", hue="month",estimator ="mean", data = df_F)


# In[49]:


sns.catplot(x= "Sex", data = df_T, hue="Pclass", col= "Survived", kind="count", height=4,aspect=.7)


# In[ ]:




