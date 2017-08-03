# get user email address
email = input("Email address?: ").strip()

# slice out the user name
user = email[:email.index("@") ]

# slice domain name
domain = email[email.index("@") + 1 :]

# format message
output = """Your username is {} and your domain name is {}""".format(user,domain)

# display output message
print(output)

