import pandas as p

df=p.read_json('/home/raja/Documents/first.json')
df.to_csv('/home/raja/Documents/pd_json_to_csv.csv',index=False)