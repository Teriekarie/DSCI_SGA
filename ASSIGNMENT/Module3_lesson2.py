# creating a parent class
class Students():
    def __init__(self, f_name, l_name, email):
        self.f_name = f_name
        self.l_name = l_name
        self.email = email

    def full_name(self):
        return '{} {} {}'.format(self.f_name, self.l_name, self.email)
    
# creating other class that derives from the Student class 
class Group_leader(Students):
    def __init__(self):
        super().__init__()
        self.student = []


# Define a method that adds a student to the list under Group_leader class
    def add_student(self, new_student):
        return self.student.append(new_student)
    
    
# Define a method that removes a student
    def remove_student(self, old_student):
        for i in self.student:
            if i == student:
               self.student.remove(old_student = i)
    
    
    def email(self):
        for i in self.student:
            print(f'{i}@stutern.com')
        
# Define a method that prints out the full names
    def student_bio(self):
        for student in self.student:
            print(student.full_name())

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

# print the full name of the student in the subcladd
female_lead.student_bio()
male_lead.student_bio()

#print the email of the instance of the subclass
female_lead.email()
male_lead.email()
