# create a class 
class Family:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

Father = Family('Jacob', 49, 'Doctor')
mother = Family('Maria', 35, 'Lawyer')

print(Father.occupation)

# Father.name = 'Jacob'
# Father.age = 49
# Father.occupation = 'Doctor'

# mother.name = 'Maria'
# mother.age = 35
# mother.occupation = 'Lawyer'

print(mother.age)
