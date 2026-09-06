import pandas as pd
# to read our csv file
df = pd.read_csv("Data.csv")
print(df)

basket = df["CUSTOMER"]
#print(basket)


print(df["Style"])

#print(type(basket))
