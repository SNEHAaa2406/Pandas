import pandas as pd
df=pd.read_csv("data.csv")
# print(df.head())
# print(df.info())
# print(df.describe())
# print(df.shape) here i used shape() so error showed up, we do not need to give the paranthesis as shape is already a attribute and not a method


#  selecting a single column
# print(df["Date"])

# s=df[["Duration","Calories"]]  here i used ([]) which was wrong you should use df first and then double brackets
# print(s)

# filtering rows
# print(df.head(5))
# print(df.describe())


# high_calories=df[df["Calories"]>400]
# print(high_calories)



# both=df[(df["Duration"] > 60)  & (df["Calories"]>30)]
# print(both)
