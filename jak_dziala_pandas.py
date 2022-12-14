import pandas as pd

data = pd.read_json('bohaterowie2.json')
data.to_csv('wyniki.csv')