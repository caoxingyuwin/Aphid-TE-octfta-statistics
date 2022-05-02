# coding: utf-8

# In[44]:


import numpy as np
import pandas as pd
#import glob
#import os

#read_path = 'D:\Rdata\\finialtxt'      # Ҫ��ȡ���ļ��еĵ�ַ
df = pd.read_csv('D:\Rdata\\finialtxt\Acyrthosiphon_pisum.clean.all.copynumber.csv.txt', \
keep_default_na=False,delimiter='\t')
# In[45]:



#df=df.fillna(0)#���NA


# In[46]:


df['Family']= df.apply(lambda x: x.Family[5:] if x.Family.startswith('Type')else x.Family,axis=1)#ȥ��type


# In[52]:


df1 = df.groupby('Family')['Copies'].sum()#����ۺ�


# In[56]:


df1.to_csv('Apres.csv',index=True)


# In[79]:


df2 = pd.read_csv('Apres.csv')
df2['Family']=df2.apply(lambda x: x.Family.split('/')[0],axis=1)#�ض��ַ���ȡ/ǰ���
df2['Family']=df2.apply(lambda x: x.Family.split('?')[0],axis=1)#�ض��ַ���ȡ��ǰ���
df3 = df2.groupby('Family')['Copies'].sum()


# In[82]:


df3.to_csv('Apres_tol.csv',index=True)

