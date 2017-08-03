students = {"Alice":24, "Bob":18}
students
students["Alice"]

students["Fred"] = 20
students["Fred"]

del students["Fred"]
students.keys()
students.values()
students.items()

# Won't work
#students.keys()[0]

# Instead
list(students.keys())[0]


