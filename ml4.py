import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load dataset
df = pd.read_csv("sales_data_sample.csv", encoding="latin1")

# Select numerical features for clustering
X = df[["SALES", "QUANTITYORDERED", "PRICEEACH", "MSRP"]]

# Handle missing values
X = X.fillna(X.mean())

# Scale the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Elbow method
wcss = []

for k in range(1, 11):
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    model.fit(X_scaled)
    wcss.append(model.inertia_)

# Plot elbow graph
plt.plot(range(1, 11), wcss, marker="o")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("WCSS")
plt.title("Elbow Method")
plt.show()

# Apply K-Means using the chosen number of clusters
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df["Cluster"] = kmeans.fit_predict(X_scaled)

# Display results
print(df[["SALES", "QUANTITYORDERED", "Cluster"]].head())
print("\nNumber of records in each cluster:")
print(df["Cluster"].value_counts())
