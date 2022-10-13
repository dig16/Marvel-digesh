#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
import json


# In[10]:


import pandas as pd


# In[3]:


import hashlib
from time import time 


# In[4]:


public = "0b0fe70a971893ef6d1965a79d1189dd"
private = "2f5a765fae583ee37883b0b292b0f1c4d100e017"
address= "http://gateway.marvel.com/v1/public/characters"


# In[6]:


ts= str(int(time()))
hash = ts + private + public
hash_result = hashlib.md5(hash.encode())


# In[7]:


api_url = "http://gateway.marvel.com/v1/public/"
public_key = input()
private_key = input()
resource = "characters"
limit = 100
ts = str(int(time()))

hash_parameter = ts+private_key+public_key

hash_result = hashlib.md5(hash_parameter.encode())

address = api_url + resource

parameter = {"apikey": '0b0fe70a971893ef6d1965a79d1189dd',

            "ts": int(time()),

            "hash": hash_result.hexdigest(),

            "limit": limit}


# In[11]:


data_frame = pd.DataFrame()
import string

start_char = list(string.ascii_lowercase + string.digits)

start_char.remove('0')

for letter in start_char :

    parameter["nameStartsWith"] = letter

    response = requests.get(address, parameter)

    temp_df = pd.json_normalize(response.json(), record_path=['data', 'results'])

    data_frame = pd.concat([data_frame, temp_df])

    del parameter["nameStartsWith"]


# In[ ]:





# In[ ]:





# In[ ]:




