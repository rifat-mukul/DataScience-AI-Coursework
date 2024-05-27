import pandas as pd

URL = 'https://en.wikipedia.org/wiki/List_of_largest_banks'

table = pd.read_html(URL)

df = table[0]

print(df)