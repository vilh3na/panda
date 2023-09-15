import pandas as pd
import matplotlib.pyplot as plt
 
a=pd.Series([10,20,30,40], ['a','b','c','d'])
print(a['b'])
print(a.iloc[1])


data = {
'Name': ['Anna', 'Bob', 'John', 'mike'],
'Age': [29, 43, 82, 23],
'Height': [176, 165, 187, 182],
'Gender': ['f', 'm', 'm','m'],
'SSN': [2123,4121,1242,1541,]}
df = pd.DataFrame (data)
df.set_index('SSN',inplace=True)
print(df)
print('here'+df['Name'].iloc[1])


print(df.count()) #quantidade de elementos em cada coluna
print(df['Age'].count())
print(df.sum()) # soma a q
for key, value in df['Age'].items() :
    print("{}:{}".format(key, value))



data = {
'SSN': [123, 445, 511, 872],
'Name': ['Anna', 'John','John', 'Mike'],
'Age': [29, 83, 42, 23],
'Height': [176, 165, 187, 182],
'Gender': ['f', 'm','m','m']}
df = pd.DataFrame (data)
df .set_index('SSN', inplace=True)
for key, value in df[ 'Age' ].items() :
    print("{}: esse{}".format (key, value))
df.sort_index(inplace=True)
print(df)
df.sort_values(by=['Name', 'Age'], inplace=True)
print (df)

names = {
'SSN': [2, 5, 7, 8],
"Name": ['Anna', 'Bob', "John", "Mike"]
}
ages = {
'SSN': [1, 2, 3, 5],
'Age': [28, 34, 45, 62]}
df1 = pd.DataFrame (names)
df2 = pd.DataFrame (ages)
df = pd.merge(df1, df2, on='SSN', how= 'left') #inner excludente outer includente, left right excludente preferencial 1a ou 2a
df.set_index('SSN' , inplace=True)
print(df)