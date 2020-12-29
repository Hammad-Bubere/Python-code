
while True:
	print ("calculater")
	print ('Enter your first Number:')
	val1=int(input())
	print ("please enter your function (-,+,*,/)")
	func=input()
	print ('Enter your second Number:')
	val2 =int(input())
	print('YourAnswer:')
	if func=="-":
		print((val1)-(val2))
	elif func=="+":
		print((val1)+(val2))
	elif func=="*":
		print((val1)*(val2))
	elif func=="/":
		print((val1)/(val2))
	else:
		print ("Enter valid function\nRecheck your entered function")
	print("Thank you! for using python calculater")
	print ('\nfor closing calculator enter (1)\nfor continue enter (2) or any number to continue')
	choice=int(input ("choice:\t"))
	if choice==1:
		print("Program Ended")
		break
		if choice==2:
			continue