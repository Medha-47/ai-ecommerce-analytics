import pandas as pd

df = pd.read_csv("data/ecommerce.csv")


print(df.duplicated().sum())