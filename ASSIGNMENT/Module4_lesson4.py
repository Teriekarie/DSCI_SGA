# program to introduce f-string
val = 'This is an example to use f-string'
print(f"{val} being used in this program.")


# how to call a method using f-string 
author = "jane smith"
a_name = author.title()
print(f"This is a book by {a_name}.")


# how to call a function with f-string
def choice(c):
  if c%2 ==0:
    return "Learn Python!"
  else:
    return "Learn JavaScript!"

print(f"Hello Python, tell me what I should learn. {choice(3)}")

# calling the function with an even number
print(f"Hello Python, tell me what I should learn. {choice(10)}")