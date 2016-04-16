# Exercises from book chapter 4

# 1. Evaluate which numbers are true

if 0 == True:
  print("0 is true")
else:
  print("0 is false")
if 1 == True:
  print("1 is true")
if 2 == True:
  print("2 is true")

# 2. Test if value is in range
#input = input("Please provide number: ")
input = 3

if input >= 0 and input <= 9:
  print("Value %d is in range" % input)
else:
  print("Value is out of range")

# 3. Test if value is in the tuple
tuple = ("first", "second")
print(tuple)

input = "first"
if tuple[0] == input:
  print("Value is in sequence on first position")
elif tuple[1] == input:
  print("Value is in sequence on second position")
else:
  print("Value is not in the sequence")

# 4. Dictionary - food in the fridge
fridge = {
  "banana" : "banana is a yellow fruit",
  "sausage" : "sausage contains meat",
  "milk" : "milk has proteins"
}

food_sought = "milk"

for i in fridge:
  if i == food_sought:
    print("Food is found in the fridge - %s : %s" % (i, fridge[i]))
    break
  else:
    print("Food not found in the fridge")

# 5. Iteration using while loop
fridge_list = fridge.keys()
current_key = fridge_list.pop()

while len(fridge_list) > 0:
  print("Current key is %s" % current_key)
  if current_key == food_sought:
    print("Food %s was found in the fridge" % food_sought)
    break
  else:
    print("Food was not found in the fridge")

  current_key = fridge_list.pop()

# 6. Exceptions handling
food_sought = "test"
try:
  print(food_sought)
  print(fridge[food_sought])
except KeyError as e:
  print("Food not found in the fridge with error: %s " % e)
