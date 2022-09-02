# program to create a dictionary containing keys

def generate_dict(number): # define a method for this
    d= {}                  # Assign an empty dictionary
    for i in range(5,16):  # Creating the range from (5,16) noting that python reads from 0
        d[i] = i ** 2
    return d
print(generate_dict(10))

