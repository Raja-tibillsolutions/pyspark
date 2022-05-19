import pandas as p

df=p.read_csv('/home/raja/Documents/first.csv')
print(df.to_csv(path_or_buf='/home/raja/Documents/pd_csv_to_json.json'))