import pandas as pd

# Load dataset
df = pd.read_csv(
    "data/ecommerce.csv",
    low_memory=False
)

print("Original Shape:", df.shape)

# Remove useless column
df.drop(columns=['Unnamed: 22'], inplace=True)

# Clean column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("-", "_")
)

# Convert date column
df['date'] = pd.to_datetime(
    df['date'],
    format='%m-%d-%y'
)

# Remove duplicates
duplicates = df.duplicated().sum()
print("Duplicates:", duplicates)

df.drop_duplicates(inplace=True)

print("Final Shape:", df.shape)

df['b2b'] = df['b2b'].astype(int)

df['amount'] = pd.to_numeric(
    df['amount'],
    errors='coerce'
)

df['amount'] = df['amount'].fillna(0)

df.drop(columns=['index'], inplace=True)

df.rename(
    columns={'date': 'order_date'},
    inplace=True
)


# Save cleaned file
df.to_csv(
    "data/cleaned_ecommerce.csv",
    index=False
)

print("Cleaned dataset saved!")