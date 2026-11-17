import pandas as pd

df = pd.read_csv("jugadors.csv")
df["age"] = df["edat"].str.extract(r"\((\d+)\)").astype(float)
market_values = df["valor_mercat"].str.replace("€","", regex = False)
market_values = market_values.str.replace("m", "", regex = False)
market_values = market_values.str.strip()
df["market_value_eur"] = pd.to_numeric(
    market_values, errors = "coerce"
) * 1_000_000
df = df.dropna(subset=["market_value_eur"])

df["goals"] = pd.to_numeric(df["gols"], errors= "coerce")
df["assists"] = pd.to_numeric(df["assistencies"], errors="coerce")
df["matches"] = pd.to_numeric(df["partits"], errors="coerce")
df["minutes_percentage"] = pd.to_numeric(
    df["percn_minuts_jugats"], errors="coerce"
)
df["position"] = df["posicio"]
df = df.dropna(
    subset = ["matches", "goals", "assists"],
    how = "all"
)
df["goals"] = df["goals"].fillna(df["goals"].median())
df["assists"] = df["assists"].fillna(df["assists"].median())
df["minutes_percentage"] = df["minutes_percentage"].fillna(df["minutes_percentage"].median())
training_data = df[[
    "goals",
    "assists",
    "minutes_percentage",
    "age",
    "position",
    "market_value_eur"
]]

training_data.to_csv("training_data.csv", index=False)

print(training_data)

print("\nMissing values:")
print(training_data.isnull().sum())
