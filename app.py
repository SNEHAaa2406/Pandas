import pandas as pd
data={
    "Name":["Sneha","Vedika","Shravani"],
    "Age":[45,8745,45],
    "City":["Kolhapur","Mumbai","Pune"]
}
df=pd.DataFrame(data)
print(df)
df.to_json("output.json",index=False)