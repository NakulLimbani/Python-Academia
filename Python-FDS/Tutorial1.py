#Ques 1
import numpy as np

#Y = np.array([ [3,6,9,12], [15,18,21,24], [27,30,33,36], [39,42,45,48],[51,54,57,60] ])
#print(Y[:,2]);
print("\n");

#print(Y[::2,1::2]);
print("\n");

#print(Y[:,::-1]);
#print(Y[:,[3,2,1,0]]);

#print(Y[::-1,::-1]);

#Ques 2
b = np.array([13, 6, 11, 19, 10, 3, 27])

#c = []
#for i in b:
    #if((i>=7) & (i<=20)):
        #c.append(i)
#print (c)


#Ques 3
x = np.array([5, 2, 5, 5, 3, 4, 3, 5, 5, 2, 5, 5, 2])
y =np.where(x==5)[0][5]
print(y)