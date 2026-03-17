# Customer Segmentation Analysis

A Streamlit-based web application that uses clustering algorithms to segment customers based on their purchasing behavior. This app allows users to upload customer datasets, select features, and visualize the resulting clusters.

## Features

- Upload customer data in CSV format or use an example dataset.
- Select features to use for clustering.
- Use K-Means clustering to identify distinct customer segments.
- Visualize customer clusters for better insights.

## Technologies Used

- **Python**: Programming language.
- **Streamlit**: Framework for building the web application.
- **Scikit-learn**: Machine learning library for clustering (K-Means).
- **Pandas**: Data manipulation and analysis.
- **Matplotlib**: Data visualization.

## Installation

Follow these steps to run the application locally:

1. Clone the repository:
      git clone https://github.com/mokshsiddhant/all-personla-projects.git
      cd all-personla-projects
2. Install required dependencies:
      pip install streamlit pandas numpy scikit-learn matplotlib
3. Run the application:
      streamlit run customer_segmentation.py
4. Open the app in your browser at:
      http://localhost:8501

Usage
Upload a CSV file containing customer data.
Ensure the dataset includes relevant features (e.g., Annual Income, Spending Score).
Select features for clustering in the sidebar.
Adjust the number of clusters using the slider.
Visualize the clusters if two features are selected.
Example Dataset
If you don't have a dataset, the app includes a sample dataset with the following columns:

CustomerID
Annual Income (k$)
Spending Score (1-100)
Screenshots
Home Page

Cluster Visualization

Future Improvements
Add support for additional clustering algorithms.
Enable 3D cluster visualizations.
Save cluster results as a downloadable file.
Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Commit your changes (git commit -m "Add feature").
Push to the branch (git push origin feature-branch).
Open a Pull Request.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Author
Developed by Moksh Siddhant
Feel free to reach out with suggestions or questions.

Acknowledgments
The Streamlit community for the amazing framework.
Scikit-learn for machine learning tools.

