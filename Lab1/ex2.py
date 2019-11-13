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
df[['price','line_total']] = df[['price','line_total']].apply(remove_dollar, axis=1)
print(df)
df[['price','line_total']] = df[['price','line_total']].astype("float")
print(df.dtypes)