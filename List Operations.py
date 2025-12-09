# Create a list
L = ["The Bodyguard", 7.0, 1992]
L

# Print the elements on each index

print('The same element using negative and positive indexing:\n Positve:',L[0],
      '\n Negative:', L[-3])

print('The same element using negative and positive indexing:\n Positve:',L[1],
      '\n Negative:', L[-2])

print('The same element using negative and positive indexing:\n Positve:',L[2],
      '\n Negative:', L[-1])


# List Slicing
L = ["The Bodyguard", 7.0, 1992, 'BG', 1]
print(L[3:5])

# Use extend to add elements to list
L = [ "The Bodyguard", 7.0]
L.extend(['pop', 10])
print(L)

# Use append to add elements to list
L = [ "The Bodyguard", 7.0]
L.append(['pop',10]) # adds list within list
print(L)

# Change the element based on the index
A = ["disco", 10, 1.2]
print('Before change:', A)
A[0] = 'hard rock'
print('After change:', A)

# Delete the element based on the index
print('Before change:', A)
del(A[0])
print('After change:', A)

# Split the string, default is by space
print('hard rock'.split())

# Split the string by comma
print('A,B,C,D'.split(','))

# Copy (copy by reference) the list A
A = ["hard rock", 10, 1.2]
B = A
print('A:', A)
print('B:', B)

# Examine the copy by reference
print('B[0]:', B[0])
A[0] = 'banana'
print('B[0]:', B[0])

# Clone (clone by value) the list A
B = A[:]
print(B)

B =[1,2,[3,'a'],[4,'b']]
print(B[3][1])


