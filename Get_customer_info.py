#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
from pymongo import MongoClient
import json

def get_customer_info(customer_id):
    client = MongoClient('mongodb+srv://dilsedigital007:wh1teMayur@cluster0.opahplu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
    mydatabase = client.RMApp
    mycollection = mydatabase.CustData
    cursor = mycollection.find({"CustomerId" : customer_id})
    listofDocuments = list(cursor)
    custdf3 = pd.DataFrame(listofDocuments)
    customer_info = custdf3
    if len(customer_info) == 0:
        print("Customer ID not found.")
        return None, None
    cust_name = customer_info['Custname'].values[0]
    sug_products = customer_info[['SugProdID1', 'SugProdName1', 'SugProdID2', 'SugProdName2', 'SugProdID3', 'SugProdName3']]
    sug_products_list = sug_products.values.tolist()[0]
    sug_products_2d = [{'SugProdID': sug_products_list[i], 'SugProdName': sug_products_list[i+1]} for i in range(0, len(sug_products_list), 2)]
    result_json = {
        'cust_name': cust_name,
        'sug_products': sug_products_2d
    }
    return json.dumps(result_json)

# Example usage:
#customer_id_input = 15737888  # Example customer ID
#result_json = get_customer_info(customer_id_input)
#print("Customer Info (JSON format):")
#print(result_json)


# In[ ]:




