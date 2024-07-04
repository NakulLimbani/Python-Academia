"""import numpy as np
A = np.array([[4 ,-1],
              [2 , 0]])
eigval , eigvec = np.linalg.eig(A)
print("Eigen Values : " ,eigval)
print("\nEigen vectors: ",eigvec)
"""

"""import numpy as np
Arr = np.random.rand(6,6)
min_val = np.min(Arr)
max_val = np.max(Arr)

print(Arr)
print(min_val)
print(max_val)"""

import numpy as np
mean = 12
std_dev = 10
Arr = np.random.normal(mean,std_dev,size=(2,3))
print(Arr)