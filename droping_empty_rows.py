import pandas as p
#This is for droping empty rows
'''df=p.read_csv('/home/raja/Documents/first.csv')
n=df.dropna()

print(n.to_csv(path_or_buf='/home/raja/Documents/drop_empty.csv'))

#This code is for fillng empty with 'NA'
df=p.read_csv('/home/raja/Documents/first.csv')
df.fillna('NA',inplace=True)
print(df.to_csv(path_or_buf='/home/raja/Documents/filling_with_NA.csv'))


#Replacing NA With Their Values
df=p.read_csv('/home/raja/Documents/first.csv')
df.replace(method='ffill',inplace=True)
print(df.to_csv(path_or_buf='/home/raja/Documents/filling_NA_withTheirvalues.csv'))

#Droping duplicates
df=p.read_csv('/home/raja/Documents/first.csv')
df.drop_duplicates('Name',inplace=True)
df.drop_duplicates('age',inplace=True)
df.drop_duplicates('phone',inplace=True)
print(df.to_csv(path_or_buf='/home/raja/Documents/drop_duplicates.csv'))


#Renaming the column Names

df=p.read_csv('/home/raja/Documents/first.csv')
df.rename(columns={'Name':'n'},inplace=True)
print(df.to_csv(path_or_buf='/home/raja/Documents/renaming_column.csv'))


#drop column
df=p.read_csv('/home/raja/Documents/first.csv')
df.drop(columns=['Name'],inplace=True)
print(df.to_csv(path_or_buf='/home/raja/Documents/drop_column.csv'))


#Select perticular columns

df=p.read_csv('/home/raja/Documents/first.csv')
print(df['Name'])

#Filtering the data on particular values
df=p.read_csv('/home/raja/Documents/first.csv')
print(df.head(2))
'''
#Add new column with static data
df=p.read_csv('/home/raja/Documents/first.csv')

df['Adrees']=['bg','bg''bg','ap','bangalore','guntur','vijyawada','hyd','chenia','pune','guntur','vijyawada','hyd','chenia','pune']

print(df.to_csv('/home/raja/Documents/adding_column.csv'))