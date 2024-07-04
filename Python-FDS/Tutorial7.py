import pandas as pd

# Load the Titanic dataset from a CSV file
titanic_data = pd.read_csv('titanic.csv')  
# Verify that the dataset is loaded correctly
print(titanic_data.head())  # Display the first few rows of the dataset


# (i) Count the number of rows and columns
num_rows, num_columns = titanic_data.shape
print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_columns}")

# (ii) Display descriptive statistics
print(titanic_data.describe())

# (iii) Select rows where 'score' is NaN
missing_score_rows = titanic_data[titanic_data['score'].isna()]
print("Rows with missing 'score':")
print(missing_score_rows)

# (iv) Get the first 4 rows
first_4_rows = titanic_data.head(4)
print("First 4 rows:")
print(first_4_rows)

# (V) Select rows where 'Age' is greater than 30 and only specific columns 'Name', 'Age', and 'Fare'
selected_data = titanic_data.loc[titanic_data['Age'] > 30, ['Name', 'Age', 'Fare']]
print("Selected data:")
print(selected_data)



