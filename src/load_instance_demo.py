import pandas as pd

# load one dataset file
df = pd.read_csv("data/10_ic_processed.csv")

# basic shape and columns
print("shape:", df.shape)
print("\ncolumns:")
print(df.columns.tolist())

# show first row
print("\nfirst row:")
print(df.iloc[0])
