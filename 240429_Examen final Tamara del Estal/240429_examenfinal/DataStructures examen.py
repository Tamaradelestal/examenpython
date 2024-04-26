import filtro
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('orders.csv')
print(df)
df_trabajo=df[['Order number','Head','Body','Legs']]
df_sorted=df.sort_values(by='Body')
print(df_sorted)
filtroAddress=df[df['Address']=='Address H']
print(filtroAddress)
sns.barplot(x='Order number', y='Address', data=df)
plt.show()
