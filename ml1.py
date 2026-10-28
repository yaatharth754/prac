
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

# 1. Load dataset
df = pd.read_csv("uber.csv")

# 2. Preprocess dataset
df.drop(columns=["key", "Unnamed: 0"], errors="ignore", inplace=True)

df["pickup_datetime"] = pd.to_datetime(
    df["pickup_datetime"], errors="coerce", utc=True
)

df.dropna(inplace=True)

# Remove invalid records
df = df[
    (df["fare_amount"] > 0) &
    (df["pickup_longitude"].between(-180, 180)) &
    (df["pickup_latitude"].between(-90, 90)) &
    (df["dropoff_longitude"].between(-180, 180)) &
    (df["dropoff_latitude"].between(-90, 90)) &
    (df["passenger_count"].between(1, 6))
].copy()

# Extract pickup hour
df["hour"] = df["pickup_datetime"].dt.hour

# Calculate distance using Haversine formula
lat1 = np.radians(df["pickup_latitude"])
lat2 = np.radians(df["dropoff_latitude"])
lon1 = np.radians(df["pickup_longitude"])
lon2 = np.radians(df["dropoff_longitude"])

a = (
    np.sin((lat2 - lat1) / 2) ** 2 +
    np.cos(lat1) * np.cos(lat2) *
    np.sin((lon2 - lon1) / 2) ** 2
)

df["distance"] = 6371 * 2 * np.arcsin(np.sqrt(a.clip(0, 1)))

# Remove zero-distance trips
df = df[df["distance"] > 0].copy()

# 3. Identify and remove fare outliers using IQR
Q1 = df["fare_amount"].quantile(0.25)
Q3 = df["fare_amount"].quantile(0.75)
IQR = Q3 - Q1

df = df[
    df["fare_amount"].between(
        max(0, Q1 - 1.5 * IQR),
        Q3 + 1.5 * IQR
    )
].copy()

print("Cleaned dataset shape:", df.shape)

# 4. Correlation analysis
features = [
    "pickup_longitude", "pickup_latitude",
    "dropoff_longitude", "dropoff_latitude",
    "passenger_count", "hour", "distance"
]

plt.figure(figsize=(9, 6))
sns.heatmap(
    df[features + ["fare_amount"]].corr(),
    annot=True, cmap="coolwarm", fmt=".2f"
)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

# 5. Split data into training and testing sets
X = df[features]
y = df["fare_amount"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 6. Train Linear Regression
lr = LinearRegression()
lr.fit(X_train, y_train)
pred_lr = lr.predict(X_test)

# 7. Train Random Forest Regression
rf = RandomForestRegressor(
    n_estimators=100, random_state=42, n_jobs=-1
)
rf.fit(X_train, y_train)
pred_rf = rf.predict(X_test)

# 8. Evaluate and compare models
results = []

for name, pred in [
    ("Linear Regression", pred_lr),
    ("Random Forest", pred_rf)
]:
    results.append({
        "Model": name,
        "R2 Score": round(r2_score(y_test, pred), 4),
        "RMSE": round(np.sqrt(mean_squared_error(y_test, pred)), 4),
        "MAE": round(mean_absolute_error(y_test, pred), 4)
    })

results_df = pd.DataFrame(results)
print("\nModel Comparison:")
print(results_df.to_string(index=False))
