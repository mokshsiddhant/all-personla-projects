print("hello world")
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Title of the App
st.title("Customer Segmentation Analysis")

# Sidebar
st.sidebar.header("Upload Customer Data")
uploaded_file = st.sidebar.file_uploader("Upload CSV File", type=["csv"])

# Default Dataset Example
if st.sidebar.button("Use Example Dataset"):
    uploaded_file = None
    example_data = {
        "CustomerID": [1, 2, 3, 4, 5],
        "Annual Income (k$)": [15, 16, 17, 18, 19],
        "Spending Score (1-100)": [39, 81, 6, 77, 40],
    }
    df = pd.DataFrame(example_data)
else:
    df = None

# Upload Data
if uploaded_file:
    df = pd.read_csv(uploaded_file)

if df is not None:
    # Display Data
    st.subheader("Customer Data")
    st.dataframe(df)

    # Select Features for Clustering
    st.sidebar.subheader("Clustering Configuration")
    features = st.sidebar.multiselect("Select Features for Clustering", df.columns)

    if len(features) >= 2:
        # Data Preprocessing
        X = df[features]
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        # Clustering
        num_clusters = st.sidebar.slider("Select Number of Clusters", 2, 10, 3)
        kmeans = KMeans(n_clusters=num_clusters, random_state=42)
        clusters = kmeans.fit_predict(X_scaled)

        # Add Cluster Labels to DataFrame
        df["Cluster"] = clusters

        # Display Clustered Data
        st.subheader("Clustered Data")
        st.dataframe(df)

        # Visualize Clusters
        st.subheader("Cluster Visualization")
        if len(features) == 2:
            plt.figure(figsize=(8, 6))
            plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=clusters, cmap="viridis", s=50)
            plt.scatter(
                kmeans.cluster_centers_[:, 0],
                kmeans.cluster_centers_[:, 1],
                s=200,
                c="red",
                marker="X",
                label="Centroids",
            )
            plt.xlabel(features[0])
            plt.ylabel(features[1])
            plt.title("Customer Clusters")
            plt.legend()
            st.pyplot(plt)
        else:
            st.warning("Visualization is available only for 2 selected features.")
    else:
        st.warning("Please select at least 2 features for clustering.")
else:
    st.info("Upload a CSV file to start or use the example dataset.")

# Footer
st.sidebar.markdown("---")
st.sidebar.write("Developed with ❤️ using Streamlit")
