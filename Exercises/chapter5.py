# Exercises for chapter 5 of the book

# 1. Write a function which adds two arguments
def do_plus(first, second):
  return first+second

first = 3
second = 5

print(do_plus(first, second))

# 2. Add type checking to verify if type is integer or string
def do_plus(first, second):
  isCorrectFirstType = type(first) == int or type(first) == str
  isCorrectSecondType = type(second) == int or type(second) == str

  if(isCorrectFirstType and isCorrectFirstType):
    return first+second
  else:
    raise TypeError("Incorrect types passed to function: first - %s, second - %s" % (first, second))

# Correct input
print(do_plus(first, second))
print(do_plus("first ", "second"))

# Incorrect input - tuple as first argument
#print(do_plus((first, second), "second"))

# 3. Extend make_omelet example

fridge = {
  'apples' : 10,
  'milk' : 2,
  'oranges' : 3
}

wanted_food = "milk"

def in_fridge():
  """Checks if fridge has a food. Fridge has to be a dictionary populated outside of this function"""

  try:
    count = fridge[wanted_food]
  except KeyError:
    count = 0

  return count

count = in_fridge()
print(count)

def make_omelet(omelet_type):
  """Dictionary with ingredients can be passed or only type of omelet"""

  if type(omelet_type) == type({}):
    print("Omelet type is a dictionary with ingredients")
    return make_food(omelet_type, "omelet")
  elif type(omelet_type) == type(""):
    omelet_ingredients = get_omelet_ingredients(omelet_type)
    return make_food(omelet_ingredients, omelet_type)
  else:
    print("I don't know how to make omelet type of type %s" % omelet_type)


def get_omelet_ingredients(omelet_name):
  """This contains dictionary of all omelet types that can be produced and their ingredients"""

  # all omelets need eggs and milk
  ingredients = {"eggs" : 2, "milk": 1}
  if omelet_name == "cheese":
    ingredients["cheddar"] = 2
  elif omelet_name == "western":
    ingredients["ham"] = 1
  else:
    print("Sorry that's not on the menu")
    return None

  return ingredients

def make_food(ingredients_needed, food_name):
  for ingredient in ingredients_needed.keys():
    print("Adding %d of %s to make a %s " % (ingredients_needed[ingredient], ingredient, food_name))

  print("Made %s" % food_name)
  return food_name

omelet_type = make_omelet("cheese")
print("Type of omelet is %s " % omelet_type)
