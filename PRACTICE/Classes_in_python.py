# create a class 
class Family:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation
        
    def parent_bio(self):
        return '{} {} {}'.format(self.name, self.age, self.occupation)
    

# defining the objects attributes
Father = Family('Jacob', 49, 'Doctor')
mother = Family('Maria', 35, 'Lawyer')

print(Father.occupation)

print(mother.parent_bio())
# merging a part of each object together with the {} place holders
print('{} {}'.format(Father.occupation, mother.age))

# Father.name = 'Jacob'
# Father.age = 49
# Father.occupation = 'Doctor'

# mother.name = 'Maria'
# mother.age = 35
# mother.occupation = 'Lawyer'

print(mother.age)
