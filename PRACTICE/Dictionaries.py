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