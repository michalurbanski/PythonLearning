# Tuples - can't be modified

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
except Exception as e:
  print("Tuple can't be modified! message: %s" % e)

# Store different elements in tuple
print("\nTuple can hold different type of elements")
multiPurposeTuple = ('first', 1)
print(multiPurposeTuple)
print(type(multiPurposeTuple[1]))

# List - can be modified
print("\nLists:")
breakfast = ["egg", "tomato"]

# Data can be also printed like in foreach loop
breakfast[0] = "toast"
for i in breakfast:
  print i

# Add elements to list
breakfast.append("bacon")
print(breakfast)

# Slicing collection
firstTwoListElements = breakfast[0:2] # start position:end position
print(firstTwoListElements)

# Take last element from list
if breakfast.pop() == "bacon":
  print("Last element taken from list")
  print(breakfast)


