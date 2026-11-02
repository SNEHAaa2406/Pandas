import pandas as pd
df=pd.read_csv("sales_data_sample.csv",encoding="Latin-1")
print(df.head(6))
print(df.tail(6))