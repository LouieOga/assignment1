import csv

def clear():
	f = open('LouieOga.csv', "w+")
	f.close()

csvfile = open('LouieOga.csv', 'a+') 

def add():
	while(True):
		arr1 = []
		idno = raw_input("enter ID no: ")
		firstname = raw_input("Enter firstname: ")
		lastname = raw_input("Enter lastname: ")
		course = raw_input("Enter course: ")
		year = raw_input("Enter year: ")
		gender = raw_input("Enter Gender: ")
		Choice = raw_input("Do you want more? (yes/no): ")
		if Choice == 'yes':
			pass
		elif Choice == 'no':
			break

	arr1.append(idno+','+firstname+','+lastname+','+course+','+year+','+gender+'\n')

	csvfile.writelines(arr1)

def view():
	file = open('LouieOga.csv')
	for line in file:
		print line

def delete():

	arr1 = []
	nput = raw_input("enter ID no: ")
	file = open('LouieOga.csv', 'r')
	for line in file:
		x = line.split(',')
		idno =x[0]
		if idno == nput:
			print "DELETED"
		else:
		
			arr1.append(line)	
	deleteThisline = open('LouieOga.csv', 'w')
	deleteThisline.writelines(arr1)
	deleteThisline.close()

def update():
	nput = raw_input("enter ID no: ")
	file = open('LouieOga.csv','r')
	arr1 = []
	for line in file:
		x = line.split(',')
		idnum = x[0]
		if idnum == nput:
			print "result: "+line
			editwhat = raw_input("enter what you want to edit: \n-firstname\n-lastname\n-course\n-year\n-gender\n\n>>>")
			if editwhat == "firstname":
				e_fname = raw_input("Enter changes: ")
				arr1.append(x[0]+','+e_fname+','+x[2]+','+x[3]+','+x[4]+','+x[5]+'\n')
			elif editwhat == "lastname":
				e_lname = raw_input("Enter changes: ")
				arr1.append(x[0]+','+x[1]+','+e_lname+','+x[3]+','+x[4]+','+x[5]+'\n')
			elif editwhat == "course":
				e_cname =  raw_input("Enter changes: ")		
				arr1.append(x[0]+','+x[1]+','+x[2]+','+e_cname+','+x[4]+','+x[5]+'\n')
			elif editwhat == "year":
				e_yname = raw_input("Enter changes: ")
				arr1.append(x[0]+','+x[1]+','+x[2]+','+x[3]+','+e_yname+','+x[5]+'\n')
			elif editwhat == "gender":
				e_gname =  raw_input("Enter changes: ")
				arr1.append(x[0]+','+x[1]+','+x[2]+','+x[3]+','+x[4]+','+e_gname+'\n')

					
		else:
			arr1.append(line)
	
	file.close()
	deleteThisline = open('LouieOga.csv', 'w')
	deleteThisline.writelines(arr1)
	deleteThisline.close()


while (True):
	Choice = raw_input("\n\n-add\n-delete\n-update\n-view\n-exit\n\n")
	if Choice == 'add':
		add()
	elif Choice == 'delete':
		delete()
	elif Choice == 'update':
		update()
	elif Choice == 'view':
		view()
	elif Choice == 'exit':
		break		


	