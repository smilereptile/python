# Ask user for name
name = input("Your name?: ")
print(type(name))

# Ask user for age
age = input("Your age?: ")
print(type(age))

# Ask user for city
city = input("Your city?: ")
print(type(city))

# Ask user what they enjoy
love = input("What do you love doing?: ")
print(type(love))

# Create output text
string = """Your name is {} and you are {} years old. You live in {} and you just love {}"""
output = string.format(name,age,city,love)

# Print output to screen
print(output)

