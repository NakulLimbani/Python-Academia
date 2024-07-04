import numpy as np
array = np.arange(20)
print(array)
'''print("Array Size:" , array.size)
print("Array Shape:" , array.shape)
print(array.reshape(4,5))
print(array.resize(2,10))

print(np.zeros((2,4)))
print(np.ones((2,3)))
print(np.full((2,3), 3.3))

print(np.empty([3,3,3]))
print(np.zeros([3,3]))
print(np.ones([3,3]))

print(np.full([3,3],2))
print(np.random.rand(3,3))

print(np.eye(3,3))
print(np.linspace(0, 6, num=4))
print(np.full_like(array,9))'''
"""
a = np.array([[1,6,3],[8,9,5],[7,2,4]])
'''print(np.geomspace(1,1000,num=4))
print(np.vander(a))'''

print(a)
print(a[-1:,-1:])"""


'''org_array = np.array([[99, 22, 33],[44, 77, 66]])
# Copying org_array to copy_array using Assignment operator
copy_array = org_array
# modifying org_array
org_array[1, 2] = 13
# checking if copy_array has remained the same
# printing original array
print('Original Array: \n', org_array)
# printing copied array
print('\nCopied Array: \n', copy_array)

import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)'''

"""arr = np.array([[1,5, 12], [2,32, 20], [3, 40, 13]])
print(arr,"\n")
print(arr.max(axis = 0))
print(arr.max(axis=1))"""

# Python program explaining
# numpy.ndarray.ndim() function

# importing numpy as geek
'''import numpy as geek

arr = [[[1, 2, 3], [4, 5, 6]],[[7,6,5],[7,9,8]]]

gfg = geek.ndim(arr)

print (gfg)'''

'''import numpy as np
# create numpy arrays x1 and x2
x1 = np.array([[1, 2],[ 0, 3]])
x2 = np.array([4, 1,2, 2])
# elementwise sum with np.add()'''
#x3 = np.add(x1, x2)
# display the arrays
'''print("x1:", x1)
print("x2:", x2)
print("x3:", x3)
x4 = x1 + x2
print(x4)'''

'''print(np.eye(4,4,-1))
print(np.identity(4))
print(x1.reshape(-1))'''

'''G = np.ndarray((1),buffer=np.array((91,8,65,3)),dtype =int)
print(G)'''

'''import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)'''
'''import numpy as np
A =np.array([[4,-1],[2,0]])
ev,egv =  np.linalg.eig(A)
print("Eigen Values:",ev)
print("Eigen vectors:",egv)'''

'''# taking multiple inputs at a time separated by comma
x = [x for x in input("Enter multiple value: ").split(",")]
print("Number of list is: ", x)
y,z,x =input().split()
print(y,z,x)
'''

'''import numpy as np
import random
arr = np.random.randint(10,size=(6,6))
print("Array\n",np.sort(arr))
print("Max value:\n",np.max(arr),"\nMin value:\n",np.min(arr))
#print("Min value:\n",np.min(arr))'''
'''
import numpy as np
mean = 12
std_dev = 10
arr = np.random.normal(mean,std_dev,size=(2,3))
print(arr)
print(np.mean(arr),np.std(arr))'''


# import numpy package
import numpy as np
'''
# create an numpy array
a = np.array([[0 ,1 ,2 ,3],
[4 ,5 ,6, 7],
[ 8, 9 ,10 ,11],
[12, 13 ,14, 15]])
'''
# display index value of 3
'''print("All index value of 3 is: ", np.where(a == 6)[0][0])

print("First index value of 3 is: ",np.where(a==3,20,a))
print(np.sort(a,axis=0))
'''
'''print(np.hsplit(a,[2,6]))

z = [(2+3j), (4-1j), (2-2j), (4-3j), (3+5j)]
print(sorted(z,key = lambda x:(x.real,x.imag)))'''


#Before sorting:
'''y= [('name','S10'), ('height',int), ('date',float)]
data = [('John', 6, 52.5 ), ('Naught', 6, 48.5 ), ('Prince', 3, 41.1 ),
('Paul', 4, 43.11)]
m = np.array(data,dtype=y)
print(m,"\n")
sorted_indices = np.sort(m,order = 'height')

print([sorted_indices])'''

'''print(np.ndarray(shape=(2,3)))
print(np.random.rand(6,2))
print(np.random.randint(10,size=(2,3)))'''
'''
import numpy as np
arr = np.array([[1, 2, 3],
[4, 5, 6], [7, 8, 9], [10, 11, 12],
[13, 14, 15], [16, 17, 18]])
newarr = np.hsplit(arr, 1)
print(newarr)'''
"""
import numpy as np
arr = np.array([[1, 2], [9, 4],[ 5, 4]])
x = np.where(arr == 4)
print(x)
print(np.argmax(arr))
print(np.max(arr))"""

# Importing numpy as np
'''import numpy as np
A = np.array([[6, 1, 1],
[4, -2, 5],
[2, 8, 7]])
# Rank of a matrix
print("Rank of A:", np.linalg.matrix_rank(A))
# Trace of matrix A
print("\nTrace of A:", np.trace(A))
# Determinant of a matrix
print("\nDeterminant of A:", np.linalg.det(A))
# Inverse of matrix A
print("\nInverse of A:\n", np.linalg.inv(A))
print("\nMatrix A raised to power 3:\n",
np.linalg.matrix_power(A, 3))'''


'''from numpy import random
x = random.poisson(lam=15, size=10)
print(x)'''
'''import random
print(np.repeat(3,4))
print(np.repeat(arr,2))
print((arr.itemsize)*(arr.size))
print(len(arr))

print(np.random.randint((10),size =(3,4,2)))
'''



