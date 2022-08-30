# example of a program to convert a given string to camelcase
# Use re.sub() to replace any - or _ with a space, using the regexp r"(_|-)+".
# Use str.title() to capitalize the first letter of each word and convert the rest to lowercase.
# use str.replace() to remove spaces between words.


from re import sub

def camel_case(s):
  s = sub(r"(_|-)+", " ", s).title().replace(" ", "")
  return ''.join([s[0].lower(), s[1:]])

# check
print(camel_case('McDonalds'))
print(camel_case('chicken-Republic'))
print(camel_case('tasties_fries'))
print(camel_case('--biggies.food'))
print(camel_case('Food-CITY'))
print(camel_case('foodVILLAGE'))
print(camel_case('food bar'))



# example of a snake case program

def snake_case(s):
  return '_'.join(
    sub('([A-Z][a-z]+)', r' \1',
    sub('([A-Z]+)', r' \1',
    s.replace('-', ' '))).split()).lower()

#check
print("\nThese are examples of the snake case")
print(snake_case('McDonalds'))
print(snake_case('chicken-Republic'))
print(snake_case('tasties_fries'))
print(snake_case('--biggies.food'))
print(snake_case('Food-CITY'))
print(snake_case('foodVILLAGE'))
print(snake_case('food bar'))
