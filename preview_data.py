import pandas as pd

df = pd.read_csv('books_prices_multi.csv')

# Remove weird characters and currency symbol, convert to float
df['price'] = df['price'].str.replace('Â£', '', regex=False).astype(float)

print(df.head())
print("\nPrice stats:")
print(df['price'].describe())
