import pandas as pd

pd.options.display.max_rows = 20

df = pd.read_csv("submission.csv")

print(df)