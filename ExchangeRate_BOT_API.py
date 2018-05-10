
# coding: utf-8

# In[34]:


import requests
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[19]:


url =     'https://iapi.bot.or.th/Stat/Stat-ReferenceRate/DAILY_REF_RATE_V1/'
querystring = {'start_period': '2018-04-15', 'end_period': '2018-04-30'}
headers = {'api-key': 'U9G1L457H6DCugT7VmBaEacbHV9RX0PySO05cYaGsm'}
response = requests.request('GET', url, headers=headers,
                            params=querystring)


# In[20]:


response.text


# In[21]:


j = pd.io.json.loads(response.text)
j


# In[22]:


j['result']['data']['data_detail']


# In[23]:


df = pd.DataFrame(j['result']['data']['data_detail'])


# In[24]:


df


# In[27]:


df.dtypes


# In[26]:


df.period = pd.to_datetime(df.period)
df.rate = pd.to_numeric(df.rate)


# In[29]:


df.set_index('period' , inplace=True)


# In[30]:


df = df.sort_index()


# In[31]:


df


# In[35]:


df.plot();

