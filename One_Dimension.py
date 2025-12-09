import numpy as np

# Creates array
a = np.array([0,1,2,3,4])
print(a)      

# Print each element

print("The first element is ",  "a[0]:", a[0])
print("The second element is ", "a[1]:", a[1])
print("The third element is ",  "a[2]:", a[2])
print("The fourth element is ", "a[3]:", a[3])
print("The fifth element is ",  "a[4]:", a[4])
print("----------------------------------------")

print(np.__version__)
print(type(a))
print(a.dtype)
print("----------------------------------------")

b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])
print(b)
print(b.dtype)
print("----------------------------------------")

c = np.array([20, 1, 2, 3, 4])
print(c)
print("The following will contain the original data")
print("c[0]:", c[0])
print("c[1]:", c[1])
print("c[2]:", c[2])
print("c[3]:", c[3])
print("c[4]:", c[4])
print("----------------------------------------")

c[0] = 100
c[4] = 0
print(c)
print("The following will contain the new data")
print("c[0]:", c[0])
print("c[1]:", c[1])
print("c[2]:", c[2])
print("c[3]:", c[3])
print("c[4]:", c[4])
print("----------------------------------------")

# Slicing operations
print(c[1:4])
d = c[1:4]
print(d)
print("d[0]:", d[0])
print("d[1]:", d[1])
print("d[2]:", d[2])
print("----------------------------------------")

# Set the fourth element and fifth element to 300 and 400

c[3:5] = 300, 400
print(c)
print("----------------------------------------")

# We can also define the steps in slicing, like this: [start:end:step].
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2])
print("----------------------------------------")

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr[1:8:2])
print("----------------------------------------")

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
for i in arr:
    if i % 2 == 0:
        print(i)
print("----------------------------------------")

b = np.array([10, 20, 30, 40, 50, 60, 70])
print("The size of array is ",b.size)
print("The dimension of the array is ",b.ndim)
print("The shape of the array is ", b.shape)
print("----------------------------------------")

# Numpy Statistical Functions
a = np.array([1, -1, 1, -1])
average = a.mean()
print("Mean:", average)
stand_dev = a.std()
print(f"Standard deviation: {stand_dev}")
print("----------------------------------------")

b = np.array([-1, 2, 3, 4, 5])
print(b)
min_b = b.min()
max_b = b.max()
print(f"The minimum is {min_b} and the maximum is {max_b}")
print("----------------------------------------")


c = np.array([-10, 201, 43, 94, 502])
c_sum = c.sum()
c_min = c.min()
c_max = c.max()
print(f"Sum: {c_sum}, Min: {c_min}, Max: {c_max}")
print("----------------------------------------")

# Array Addition
u = np.array([1,0])
print("u:", u)
v = np.array([0,1])
print("v:", v)
z = np.add(u,v) # linear transformation
print("z:",z)
print("----------------------------------------")

# My solution to the last exercise

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])
even = []
odds = []
for i in arr1:
    if i % 2 == 0:
        even.append(i)
    elif i % 2 != 0:
        odds.append(i)
        
print(np.array(even))
print(np.array(odds))
print("----------------------------------------")

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])
even = []
odds = []
for i in arr2:
    if i % 2 == 0:
        even.append(i)
    elif i % 2 != 0:
        odds.append(i)
        
print(np.array(even))
print(np.array(odds))
print("----------------------------------------")









