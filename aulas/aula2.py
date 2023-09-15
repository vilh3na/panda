import pandas as pd

df=pd.read_csv('people.csv',delimiter=',')
df.set_index('SSN',inplace=True)
print(df)
print(df.loc[df['Age'] == 45])  
#acima de 170 e menos de 50
print(df.loc[(df['Age']<50) & (df['Height']<170)]['Name'])