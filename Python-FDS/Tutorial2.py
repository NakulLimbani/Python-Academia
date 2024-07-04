#Ques 1
import numpy as np
#a = np.array([[5.24, 3.28, 6.99], [3.24, 5.82, 2.39], [2.54, 3.39, 6.39]])
#Ques 1(1)
#print(np.sum(a))
#print(np.sum(a,axis=1))
#print(np.sum(a,axis=0))

#Ques 1(2)
#print(np.where(a==5.32,15.32,a))
#print(np.where(a<5.32,15.32,a))
#print(np.where(a>5.32,15.32,a))

#Ques 1(3)
#axis = 0 ==> Column , axis = 1 ==> Row
#print(np.sort(a,axis=1))
#print(np.sort(a,axis=0))

#Ques1(4)
b = np.array([[ 0, 1, 2, 3],
[ 4, 5, 6, 7],
[ 8, 9, 10, 11],
[12, 13, 14, 15]])
#print(np.hsplit(b, [3, 4]))

#Ques 2
# Original complex array
c = [(2+3j), (4-1j), (2-2j), (4-3j), (3+5j)]

# Sort the array based on real part and then imaginary part
#print(sorted(c, key=lambda x: (x.real, x.imag)))

import numpy as np

# Define the structured array with names, height, and class

data = np.array([('John', 6, 52.5),
        ('Naught', 6, 48.5),
        ('Prince', 3, 41.1),
        ('Paul', 4, 43.11)])
sorted_indices = np.argsort(data[:,1])
print(data[sorted_indices])




