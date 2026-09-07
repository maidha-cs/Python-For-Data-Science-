import numpy as np
lst = [1,2,3,4,5]
arr= np.array(lst)
print(arr)
kind= type(arr)
print(kind)
size= arr.shape
# .shape 
print (size)
# now we can make 2D array:
lst1 = [1,3,5,7,9]
lst2 = [2,4,6,8,10]
lst3 = [1,3,5,7,9]
arr2D = np.array([lst1,lst2,lst3])
print(arr2D)

