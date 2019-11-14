import pandas as pd
import matplotlib.pyplot as plt
import seaborn
import re
def remove_dollar_2(args):
    return pd.Series([args['price'].replace("$",""), args['line_total'].replace("$","")])
def remove_dollar(arg):
    return arg.replace("$","")
df = pd.read_csv('sales.csv')
df['ordered_at'] = pd.to_datetime(df['ordered_at'])
print(df)
# df[['price','line_total']] = df[['price','line_total']].apply(remove_dollar_2, axis=1)
# for index, row in df.iterrows():
#     df.loc[index,'price']= row['price'].replace("$","")
#     df.loc[index,'line_total'] = row['line_total'].replace("$","")

df['price'] = df['price'].str.replace("$","")
df['line_total'] = df['line_total'].str.replace("$","")

print(df)
df[['price','line_total']] = df[['price','line_total']].astype("float")
print(df.dtypes)
x = df.duplicated()
print(x)