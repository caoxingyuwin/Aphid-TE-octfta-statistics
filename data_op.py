#!/usr/bin/env python
# coding: utf-8

# In[44]:


import pandas as pd
import glob
import os

read_path = 'D:\Rdata\\finialtxt'      # 要读取的文件夹的地址
read_csv = glob.glob(os.path.join(read_path,'*.txt')) # 读取文件夹中所有后缀为txt的文件地址
df = None
for i,path in enumerate(read_csv):
    new= pd.read_csv(path,delimiter='\t')
    if df is None:
        df = new
    else:
        df = pd.concat([df,new])  # 之后读取的每个文件都与前一个文件合并


# In[45]:



df=df.fillna(0)#填充NA


# In[46]:


df['Family']= df.apply(lambda x: x.Family[5:] if x.Family.startswith('Type')else x.Family,axis=1)#去掉type


# In[52]:


df1 = df.groupby('Family')['Copies'].sum()#分组聚合


# In[56]:


df1.to_csv('res.csv',index=True)


# In[79]:


df2 = pd.read_csv('res.csv')
df2['Family']=df2.apply(lambda x: x.Family.split('/')[0],axis=1)#截断字符串取/前面的
df2['Family']=df2.apply(lambda x: x.Family.split('?')[0],axis=1)#截断字符串取？前面的
df3 = df2.groupby('Family')['Copies'].sum()


# In[82]:


df3.to_csv('res_tol.csv',index=True)

