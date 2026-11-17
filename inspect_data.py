import pandas as pd

# Load the dataset
df = pd.read_csv("jugadors.csv")

# Show examples of the values we need to clean
print("Age examples:")
print(df["edat"].head(15).to_string(index=False))

print("\nMarket value examples:")
print(df["valor_mercat"].head(15).to_string(index=False))

print("\nPosition examples:")
print(df["posicio"].unique())

print("\nMinutes percentage examples:")
print(df["percn_minuts_jugats"].head(15).to_string(index=False))