print ('enter amount:')
while True:
	m=int(input ())
	if m>0 and m<5000:
		print ("you are able to get money")
	if m==5000:
		print('you can withdraw money')
	if m==0 :
		print ("please enter valid amount")
	if m<0:
		print ("please enter valid amount")
	if m>5000:
		print('we are not able to give money more then "5000"')
	else:
		print("Thank you")
		print('for exist Task enter "1"\n& for continue enter "2"')
	inp=int(input())
	if inp == 1:
		print('Task complited')
		break
	if inp == 2:
		print('New Task')
		continue
	if inp != 1 or 2:
		print('you enter incorrect choice\nTask is countiued')
