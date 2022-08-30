# creating a parent class
class Students():
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def full_name(self):
        return '{} {} {}'.format(self.name, self.email)
    
# creating other class that derives from the Student class 
class Group_leader(Students):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.student = []


# Define a method that adds a student to the list under Group_leader class
    def add_student(self, new_student):
        return self.student.append(new_student)
    
    
# Define a method that removes a student
    def remove_student(self, old_student):
        for i in self.student:
            if i == old_student:
               self.student.remove(old_student)
    
    
# create 3 more instances of the parent class
class_rep = Students()
course_rep = Students()
Assignments_rep = Students()

# create 2 instances of the sub class
female_lead = Group_leader()
male_lead = Group_leader()

# Add 2 students each to the list of students in subclass instances
female_lead.add_student("Darling Law")
female_lead.add_student("Ally Shepard")

male_lead.add_student("Joe Jonas")
male_lead.add_student("Mark Lee")


# remove 1 student each from the instance of the sub class
female_lead.remove_student("Mark Lee")
male_lead.remove_student("Darling Law")

# print the full name of the student in the subclass
female_lead = Group_leader("Ally Shepard", "allyyShep@gmail.com")
male_lead = Group_leader("Mark Lee", "leemark@gmail.com")

print(female_lead.name)
print(male_lead.name)

#print the email of the instance of the subclass
print(female_lead.email)
print(male_lead.email)
