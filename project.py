import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline
import seaborn as sns  # type: ignore
df  = pd.read_csv(r'C:\Users\deepb\OneDrive\Desktop\PowerBi Project\pythonprojectDA\Diwali Sales Data.csv', encoding='unicode_escape')
df.shape
df.head(10)
#df.info()
df.drop(['Status','unnamed1'], axis=1,inplace=True)
df.info()
#Check for null value
pd.isnull(df).sum()
#df.shape
df.dropna(inplace=True)
df.shape
#initilize list of list
data_test = [['Deep',11],['Somnath',15],['Joyeeta', ],['Brototi', 16]]
df_test = pd.DataFrame(data_test, columns=['Name', 'Age'])
df_test
df_test.dropna()
df_test
df.dropna(inplace=True)
# change data type
df['Amount'] = df['Amount'].astype('int')
df['Amount'].dtypes
df.columns
#rename column
df.rename(columns= {'Marital_Status':'Shaadi'})
# describe() method returns description of the data in the DataFrame (i.e. count, mean, std, etc)
df.describe()
# use describe() for specific columns
df[['Age', 'Orders', 'Amount']].describe()
# plotting a bar chart for Gender and it's count

ax = sns.countplot(x = 'Gender',data = df)

for bars in ax.containers:
    ax.bar_label(bars)
    
