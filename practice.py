"""import numpy as np
a =[5, 2, 7,6], [9 , 2 ,55, 58.5], [2, 3, 40.4, 6]
arr = np.array(a)

"""

'''print(arr)
print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.dtype)
print(type(arr))
print((arr.shape))
print (type(arr.ndim))
print(arr.dtype)'''



"""print ( arr/2)
print(arr//2)
print(arr**3)
print(arr-arr)
print(arr*arr)
print(arr+arr)
print(arr/arr)
print(arr//arr)
print(arr%2)"""



'''print(arr.astype(np.int32))
print(arr.astype(np.float64))'''

"""
import numpy as np
arr = np.array([1,2,3,4,5,6,7])
print(arr[1:5])
"""




#PANDAS
"""import pandas as pd
data = {
    "Cars" : ["Jaguar" , "Volvo" , "BMW" , "Mercedes"],
    "Rank" : ["1" , "2" , "4" , "3"]
}
table = pd.DataFrame(data)
print(table)"""

"""import pandas as pd
a = {"Jaguar" : 1  , "Volvo" : 2 , "BMW" : 4 , "Mercedes" : 3}
myvar = pd.Series(a,index=["Jaguar","Volvo"])
print(myvar)"""


"""# Import pandas package
import pandas as pd

# Define a dictionary containing employee data
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
'Age':[27, 24, 22, 32],
'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
'Qualification':['Msc', 'MA', 'MCA', 'Phd']}

# Convert the dictionary into DataFrame 
df = pd.DataFrame(data)

# select two columns
print(df[['Name', 'Qualification']])"""



'''# importing pandas as pd
import pandas as pd
# importing numpy as np
import numpy as np
# dictionary of lists
dict = {'First Score':[100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score':[np.nan, 40, 80, 98]}
# creating a dataframe from list
df = pd.DataFrame(dict)
# using isnull() function  
print(df.notnull()) # OR print(df.isnull())
'''

'''
#QUERY
import pandas as pd

data = {
  "name": ["Sally", "Mary", "John"],
  "age": [50, 40, 30]
}

df = pd.DataFrame(data)

print(df.query('age <50'))
'''
#SLICING
import numpy as np
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[:,2])
print(arr2d[1:2,1:])
