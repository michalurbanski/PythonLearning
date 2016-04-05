# Tuples

tuple = ('first', 'second', 'third')
print(tuple)

print("This is tuple printed using formatted string: %s %s %s" % tuple)

# Iterate over tuple elements

print("\nPrinting tuple using for loop")
for i in range(len(tuple)): # Note colon at the end of 'for' statement
  print(tuple[i])

# Tuple elements can't be modified

try:
  tuple[0] = 'new element'
except:
  print("Tuple can't be modified!")

# Store different elements in tuple
print("\nTuple can hold different type of elements")
multiPurposeTuple = ('first', 1)
print(multiPurposeTuple)
print(type(multiPurposeTuple[1]))
