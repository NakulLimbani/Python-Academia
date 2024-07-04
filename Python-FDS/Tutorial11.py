# (i) Univariate Analysis on Sepal Length:

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset from the given URL
url = "https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv"
iris_df = pd.read_csv(url)

# Filter the dataset for the specified species
species_to_include = ["setosa", "virginica", "versicolor"]
filtered_df = iris_df[iris_df['species'].isin(species_to_include)]

# Univariate analysis on sepal length
plt.figure(figsize=(8, 6))
sns.histplot(data=filtered_df, x='sepal_length', kde=True)
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.title('Univariate Analysis - Sepal Length for Setosa, Virginica, Versicolor')
plt.show()



# (ii) Bivariate Analysis on Sepal Length ad Sepal Width:
# Bivariate analysis on sepal length and sepal width
plt.figure(figsize=(8, 6))
sns.scatterplot(data=filtered_df, x='sepal_length', y='sepal_width', hue='species')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.title('Bivariate Analysis - Sepal Length vs. Sepal Width')
plt.show()

# (iii) Perform multivariate analysis on the given data.
# Multivariate analysis using pair plots
plt.figure(figsize=(10, 8))
sns.pairplot(data=filtered_df, hue='species', diag_kind='kde', markers=["o", "s", "D"])
plt.suptitle('Multivariate Analysis - Pair Plots')
plt.show()
