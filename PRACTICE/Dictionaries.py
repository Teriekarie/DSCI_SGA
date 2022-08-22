# program t create a menue dictionary
menue = {"avocado toast": 6, "carrot juice": 5, "bleberry muffin": 2}

print(type(menue))

# Ading a key
menue["cheesecake"] = 7

# Adding the new key ti the dictionary
menue = {"avocado toast": 6, "carrot juice": 5, "bleberry muffin": 2, "cheesecake": 7}

# Adding multiple keys
menue.update({"banana": 6, "lemonade": 5, "parfait": 4})

print(menue)

# Dictionary comprehension
names = ["Ada", "Bola", "Fay", "Dolapo", "Yinka"]
age = [30, 26, 27, 35, 25]

students = {key:value for key, value in zip(names, age)}
print(students)

# calling out an element from the dictionary
print(menue["banana"])
print(students["Bola"])

# Using the get() method
print(menue.get("lemonade"))

# Removing elements from a dictionary
print(students.pop("Fay"))

# Randomly removes an item 
print(students.popitem())

# Removing all item from dictionary
students.clear()
print(students)

# creating a dictionary with key value pairs as num:squares
# numbers with range of 6
Box = {}
for x in range(8):
    Box[x] = x*x
    print(Box)

Box = {x: x*x for x in range(8)}
print(Box)

