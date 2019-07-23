student = [ ]

print("Hello there.")

checker = True
	
while checker == True:
	
	print("1. Add student")
	print("2. Remove Student")
	print("3. Update Student")
	print("4. Read List")
	print("5. Exit")

	number = int(input("Please enter a number."))
	print("-----------------------------------------------")

	if number == 1:
		name = input("Enter a name: ")
		student.append(name.upper())
		print("-----------------------------------------------")
		
		print("Student added.")
		print("-----------------------------------------------")

	
	elif number == 2:
		name = input("Enter a name: ")
		student.remove(name.upper())
		print("Student removed.")
		print("-----------------------------------------------")

	
	elif number == 3:
		print(student)
		num2 = int(input("Which Index?"))
		print(student[num2] + " selected. Change to?")
		print("-----------------------------------------------")
		
		new = input()
		student[num2] = new.upper()
		
		print("Change successful.")
		print("-----------------------------------------------")
		
	elif number == 4:
		print(student)
		print("-----------------------------------------------")

	elif number == 5:
		print("Done.")
		print("-----------------------------------------------")
		break
	
	else:
		print("Number from 1-5")
		print("-----------------------------------------------")