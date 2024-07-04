
import pandas as pd

# (i) To split a dataset to group by two columns and count by each row. 
# Create a DataFrame from the provided data
data = {
    'ord_no': [70001, 70009, 70002, 70004, 70007, 70005, 70008, 70010, 70003, 70012, 70011, 70013],
    'purch_amt': [150.50, 270.65, 65.26, 110.50, 948.50, 2400.60, 5760.00, 1983.43, 2480.40, 250.45, 75.29, 3045.60],
    'ord_date': ['05-10-2022', '09-10-2022', '05-10-2022', '08-17-2022', '10-09-2022', '07-27-2022', '10-09-2022', '10-10-2022', '10-10-2022', '06-17-2022', '07-08-2022', '04-25-2022'],
    'customer_id': [5001, 5001, 5005, 5001, 5005, 5001, 5005, 5001, 5005, 5001, 5005, 5005],
    'salesman_id': [5002, 5005, 5001, 5003, 5002, 5001, 5001, 5006, 5003, 5002, 5007, 5001]
}

df = pd.DataFrame(data)

# Split the dataset and count rows for each combination of customer_id and salesman_id
grouped = df.groupby(['customer_id', 'salesman_id']).size().reset_index(name='count')

# Display the result
print(grouped)


# (ii) Construct a Pandas program to split the following dataframe into groups, group by month and year based on order date and
# find the total purchase amount year wise, month wise and salesman wise.

import pandas as pd

# Create a DataFrame from the provided data
data = {
    'ord_no': [70001, 70009, 70002, 70004, 70007, 70005, 70008, 70010, 70003, 70012, 70011, 70013],
    'purch_amt': [150.50, 270.65, 65.26, 110.50, 948.50, 2400.60, 5760.00, 1983.43, 2480.40, 250.45, 75.29, 3045.60],
    'ord_date': ['05-10-2022', '09-10-2022', '05-10-2022', '08-17-2022', '10-09-2022', '07-27-2022', '10-09-2022', '10-10-2022', '10-10-2022', '06-17-2022', '07-08-2022', '04-25-2022'],
    'customer_id': [5001, 5001, 5005, 5001, 5005, 5001, 5005, 5001, 5005, 5001, 5005, 5005],
    'salesman_id': [5002, 5005, 5001, 5003, 5002, 5001, 5001, 5006, 5003, 5002, 5007, 5001]
}

df = pd.DataFrame(data)

# Convert the 'ord_date' column to a datetime object
df['ord_date'] = pd.to_datetime(df['ord_date'], format='%m-%d-%Y')

# Group by year, month, and salesman, and find the total purchase amount
result = df.groupby([df['ord_date'].dt.year, df['ord_date'].dt.month, 'salesman_id'])['purch_amt'].sum()

# Rename the columns for clarity
result.columns = ['Year', 'Month', 'Salesman', 'Total Purchase Amount']

# Display the result
print(result)


# (iii) To split the following dataframe into groups based on all columns and calculate
# Groupby value counts on the dataframe.

import pandas as pd

# Create a DataFrame from the provided data
data = {
    'id': [1, 2, 1, 1, 2, 1, 2],
    'type': [10, 15, 11, 20, 21, 12, 14],
    'book': ['C', 'C++', 'Java', 'C', 'C++', 'Java', 'C++']
}

df = pd.DataFrame(data)

# Group by all columns and calculate value counts
grouped = df.groupby(df.columns.tolist()).size().reset_index(name='count')

# Pivot the table to get the desired output
pivot_table = grouped.pivot(index=['id', 'type'], columns='book', values='count').fillna(0).reset_index()

# Display the result
print(pivot_table)



# (iv) To split a given dataframe into groups with multiple aggregations.
import pandas as pd

# Create a DataFrame from the provided data
data = {
    'College': ['S1', 'S2', 'S3', 'S4', 'S5', 'S6'],
    'sem': ['s001', 's002', 's003', 's001', 's002', 's004'],
    'name': ['V Alberto Franco', 'V Gino Mcneill', 'VI Ryan Parkes', 'VI Eesha Hinton', 'V Gino Mcneill', 'VI David Parkes'],
    'date_Of_Birth': ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997'],
    'age': [18, 18, 19, 19, 20, 20],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']
}

df = pd.DataFrame(data)

# Group by 'College' and 'sem' and perform multiple aggregations
aggregated = df.groupby(['College', 'sem']).agg({
    'name': 'first',  # Get the first name in each group
    'date_Of_Birth': 'max',  # Get the maximum date_Of_Birth in each group
    'age': 'mean',  # Calculate the mean age in each group
    'height': 'max',  # Get the maximum height in each group
    'weight': 'min',  # Get the minimum weight in each group
    'address': 'first'  # Get the first address in each group
}).reset_index()

# Display the result
print(aggregated)



# (V) to split a given dataframe into groups and display target column as a list of uniquevalues.

import pandas as pd

# Create a DataFrame from the provided data
data = {
    'id': ['A', 'A', 'B', 'B', 'B', 'B', 'C', 'C', 'C', 'C', 'C'],
    'type': [1, 1, 1, 1, 2, 2, 1, 1, 1, 2, 2],
    'book': ['C', 'C', 'C++', 'Java', 'C', 'C++', 'Java', 'DS', 'DS', 'DS', 'Java']
}

df = pd.DataFrame(data)

# Group by 'id' and 'type' and display the 'book' column as a list of unique values
result = df.groupby(['id', 'type'])['book'].unique().reset_index()

# Display the result
print(result)


