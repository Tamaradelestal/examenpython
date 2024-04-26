import pymongo
import pandas as pd
import matplotlib.pyplot as plt

uri="mongodb+srv://Tamaradelestalexamen:examenfinalBI@cluster0.folvppn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
conexion=pymongo.MongoClient(uri)
print(conexion)
db=conexion['examen1']
coleccion=db['productos']
data=list(coleccion.find())
df=pd.DataFrame(data)
print(df)
plt.figure(figsize=(6,6))
df['precio'].value_counts().plot(kind='pie',autopct='%1.1f%%',startangle=140)
plt.show()
