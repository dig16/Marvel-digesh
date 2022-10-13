#!/usr/bin/env python
# coding: utf-8

# In[2]:


from time import time
import requests
import pandas as pd
from pprint import pprint as pp
from asyncio.windows_events import NULL
import hashlib
import argparse


# In[2]:


def dig_fun(nameStartsWith,  hash_ , API_key):   #giving default value as null helps us in giving a clearer error message to the user



    address="http://gateway.marvel.com/v1/public/characters"   #url



    parameters={"apikey":API_key,"hash":hash_,"ts":int(time()),"limit":100,"nameStartsWith":nameStartsWith} #define all the parameters and keys
    
    response=requests.get(address,parameters) #we are using url alongwith api key(public) as well as hash key and also by inducing the parameters nameStartswith and limit
    print(response.json)    



    df = pd.json_normalize(response.json(), record_path=['data', 'results'])
    
    return df


# In[3]:


api_url = "http://gateway.marvel.com/v1/public/"
args.public = '0b0fe70a971893ef6d1965a79d1189dd'
args.private = '2f5a765fae583ee37883b0b292b0f1c4d100e017'
resource = "characters"

limit = 100


# In[7]:


ts = str(int(time()))
hash_params = ts+args.private+args.public
hash_result = hashlib.md5(hash_params.encode())

df = dig_fun(nameStartsWith = "Captain", hash_ = hash_result.hexdigest(), API_key = public_key)


# In[10]:


#activity 4 
def dig_filter(dataf1,col,filter_condition):
    return dataf1.query(col+filter_condition)   #optimal method for the above code.

# def ch_filter1(df1,col,filter_condition):
#     total_condition = col+filter_condition;
#     res = (df1.query(total_condition));  #code to define and convert to df for a filter conditionbased on selected column and the condition on that column
#     return res 

result2= dig_filter(dataf1=df, col='name',filter_condition='.str.startswith("C")')
print("-----ACTIVITY: 4-----")
print("Result: Characters Starting with 'C'",result2)


# In[7]:


parser = argparse.ArgumentParser()
args = parser.parse_args()

parser.add_argument("0b0fe70a971893ef6d1965a79d1189dd", type=str)

parser.add_argument("2f5a765fae583ee37883b0b292b0f1c4d100e017", type=str)


# In[ ]:




