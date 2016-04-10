# Exercises from book chapter 3

# 1. List of diary products
dairy_section = ['Cheese', 'Milk', 'Butter', 'Cream']

# 2. Print first and last element
first = dairy_section[0]
last = dairy_section[len(dairy_section)-1]
print("First is %s, Last is %s" % (first, last))

# 3. Tuple with expiration date parts
milk_expiration = (12, 10, 2009)

# 4. Print values from the tuple
print("This milk carton will expire on %d/%d/%d" % (milk_expiration[0], milk_expiration[1], milk_expiration[2]))

# 5. Create dictionary
milk_carton = {
  "expiration_date" : milk_expiration,
  "fl_oz" : 12,
  "cost" : 2,
  "brand_name" : "unknown"
}

# 6. Print values of all dictoinary elements
for i in milk_carton:
  print("%s: %s" % (i, milk_carton[i]))

# 7. Calculate cost of six cartons of milk
number = 6
print("Cost of six cartons of milk is %d" % (number*milk_carton["cost"]))

# 8. Create list of cheeses and append to dairy_section
cheeses = ["Emmentaler", "Gouda", "Edam"]
dairy_section.extend(cheeses)
print(dairy_section)

for i in cheeses:
  dairy_section.remove(i)

print(dairy_section)

# 9. Count number of cheeses in the list
print("Number of cheeses is %d" % len(cheeses))

# 10. First five letters of first cheese
first_cheese = cheeses[0]
print("First five letters of first cheese are: %s" % first_cheese[0:5])
