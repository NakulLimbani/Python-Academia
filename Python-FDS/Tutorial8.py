import pandas as pd

# Load the Titanic dataset from a CSV file
titanic_data = pd.read_csv('titanic.csv')  


# (i) Select the rows where age of passengers is less than 21 and greater than 40
selected_age_range = titanic_data[(titanic_data['Age'] < 21) & (titanic_data['Age'] > 40)]

# (ii) Change the age in row for passenger 12 to 48
titanic_data.at[11, 'Age'] = 48

# (iii) Split the dataframe by PClass and get mean, min, and max value of age for each class
age_stats_by_class = titanic_data.groupby('Pclass')['Age'].agg(['mean', 'min', 'max'])

# (iv) Replace the mean of age for the missing data
mean_age = titanic_data['Age'].mean()
titanic_data['Age'].fillna(mean_age, inplace=True)


# Display the results
print("Selected rows with age between 21 and 40:")
print(selected_age_range)

print("Age of passenger 12 changed to 48:")
print(titanic_data.loc[11])  # Displaying the updated row

print("Age statistics by PClass:")
print(age_stats_by_class)

print("Missing age values replaced with mean age:")
print(titanic_data)
