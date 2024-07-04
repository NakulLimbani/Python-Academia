# (i) Create a Pie Chart for Male/Female Proportion:

import pandas as pd
import matplotlib.pyplot as plt

# Load the Titanic dataset
# Replace 'titanic_dataset.csv' with the path to your dataset
titanic_df = pd.read_csv('titanic_dataset.csv')

# Count the number of male and female passengers
gender_counts = titanic_df['Sex'].value_counts()

# Create a pie chart
plt.figure(figsize=(6, 6))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightcoral'])
plt.title('Male/Female Proportion on Titanic')
plt.show()


# (ii) Create a Scatter Plot of Fare Paid vs. Age, Differ the Plot Color by Gender:

import seaborn as sns

# Create a scatter plot with color differentiation by gender
plt.figure(figsize=(8, 6))
sns.scatterplot(data=titanic_df, x='Age', y='Fare', hue='Sex')
plt.title('Scatter Plot of Fare Paid vs. Age (Color by Gender)')
plt.show()


# (iii) Calculate the Number of People Who Survived:
#You can count the number of survivors in the dataset:

num_survived = titanic_df['Survived'].sum()
print(f'Number of people who survived: {num_survived}')

# (iv) Create a Histogram of Fare Paid:
# Create a histogram of Fare Paid
plt.figure(figsize=(8, 6))
sns.histplot(titanic_df['Fare'], bins=30, kde=True, color='skyblue')
plt.xlabel('Fare Paid')
plt.ylabel('Count')
plt.title('Histogram of Fare Paid')
plt.show()