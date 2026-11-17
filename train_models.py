import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline


# pandas: Reads and organizes our training data
# joblib: Saves our trained model to a file
# train_test_split: Separates data into training and testing sets
# LinearRegression: Creates our prediction model
# mean_absolute_error: Measures average prediction error
# ColumnTransformer: Applies different preprocessing to different columns
# OneHotEncoder: Converts positions into numeric features
# Pipeline: Combines preprocessing and prediction into one model

df = pd.read_csv("training_data.csv")

features = ["goals", "assists", "minutes_percentage", "age", "position"]

X = df[features]
y= df["market_value_eur"]/ 1_000_000

preprocessor = ColumnTransformer([
    ("position", OneHotEncoder(handle_unknown="ignore"), ["position"])
], remainder="passthrough")

#OneHotEncoder creates seperate colums for each position.

model = Pipeline([
    ("preprocessor", preprocessor),
    ("regression", LinearRegression())
])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

model.fit(X_train, y_train)
#.fit() tells the model to learn the relationship between player statistics and their market values.

predictions = model.predict(X_test)
error = mean_absolute_error(y_test, predictions)
print(f"Average error:€{error:.2f}M ")

joblib.dump(model, "model.pkl")

print("Model saved!"    )
