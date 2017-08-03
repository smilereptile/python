known_users = [ "Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Georgie", "Harry" ]

print (len(known_users))

while True:
   print ("Hi! My name is Travis")
   name = input("""What's your name ?: """).strip().capitalize()

   if name in known_users:
      print("name recognized")
      remove = input("Would you like to be removed from the system (y/n)?: ").lower()
      if remove == "y":
         known_users.remove(name)
         print(known_users)
   else:
      print("name NOT recognized")
      add_me = input("Would you like to be added to the system (y/n)?: ").strip().lower()
      if add_me == "y":
         known_users.append(name)


	
