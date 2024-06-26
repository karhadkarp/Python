#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from pymongo import MongoClient


#custdf= pd.read_csv('CustData.csv')
#productdf = pd.read_csv('productData.csv')
#custID = 15701354
#productID = 4

#***********HardCode Values************************ 
custID = 15737888
productID = 2


client = MongoClient('mongodb+srv://dilsedigital007:wh1teMayur@cluster0.opahplu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

mydatabase = client.RMApp
mycollection = mydatabase.CustData
cursor = mycollection.find({"CustomerId" : custID})
listofDocuments = list(cursor)
custdf2 = pd.DataFrame(listofDocuments)
#custdf2
# Need col
custdf2[['Custname', 'CreditScore','Geography','Gender','Age','Tenure','Balance','NumOfProducts','HasCrCard','IsActiveMember','EstimatedSalaryOrIncome']]

mycollection = mydatabase.productData
cursor = mycollection.find({"ProductID" : productID})
listofDocuments = list(cursor)
productdf2 = pd.DataFrame(listofDocuments)

#productdf2 = productdf.query('ProductID == @productID')
#productdf2

Customer_Name = custdf2['Custname'].to_string(index=False)
Customer_Credit_Score = custdf2['CreditScore'].to_string(index=False)
Customer_Geography = custdf2['Geography'].to_string(index=False)
Customer_Gender = custdf2['Gender'].to_string(index=False)
Customer_Age = custdf2['Age'].to_string(index=False)
Customer_Tenure = custdf2['Tenure'].to_string(index=False)
Customer_Balance = custdf2['Balance'].to_string(index=False)
Customer_NoOfProducts = custdf2['NumOfProducts'].to_string(index=False)
Customer_HasCrCard = custdf2['HasCrCard'].to_string(index=False)
Customer_Active = custdf2['IsActiveMember'].to_string(index=False)
Customer_SalaryOrIncome = custdf2['EstimatedSalaryOrIncome'].to_string(index=False)

pd.options.display.max_colwidth = 200 
Product_Name = productdf2['ProductName'].to_string(index=False)
Product_Features = productdf2['Features'].to_string(index=False)

custbackground = f'Customer Name is {Customer_Name}.{Customer_Name} is a {Customer_Age} years old {Customer_Gender} living in {Customer_Geography}. {Customer_Name} is having a relationship with bank since past {Customer_Tenure} years. {Customer_Name} is having credit score of {Customer_Credit_Score}. Current balance in {Customer_Name}s account is {Customer_Balance}$.{Customer_Name} is using total {Customer_NoOfProducts} banking products with the bank.{Customer_Name} is also has a credit card with bank. Average salary or income of {Customer_Name} is {Customer_SalaryOrIncome}'
custbackground2 = f'Customer Name : {Customer_Name},Age : {Customer_Age} years,Gender : {Customer_Gender} ,Location : {Customer_Geography},Relationship with bank : past {Customer_Tenure} years,credit score : {Customer_Credit_Score} ,Current balance : {Customer_Balance}$,Total Products used : {Customer_NoOfProducts}  ,Average salary or income : {Customer_SalaryOrIncome}$'


context = 'I am a Relationship manager working with the reputed bank.I like to send a mail to the one of my customer regarding sale of a product. Following are the customer details'
guidelines = 'While writing mail follow these guidelines : 1. writes a personilised mail to customer. 2. consider the all details provide to make mail more personlised but don not quote exact figures like account balance or credit score. '  
productDetails = f'Below are product details which I try to sale from this email . Product Name : {Product_Name} Product Features : {Product_Features}'
promt = context + custbackground2 + guidelines + productDetails
promt


# In[ ]:




