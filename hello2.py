try:
	x = input('Enter Hours\n')
	Hours = int(x)
	y = input('Enter Rate\n')
	Rate = int (y)
	if Hours > 40:
		pay = (1.5 * Rate * (Hours - 40)) + (40 * Rate)
	else:
		pay = Rate * Hours
	print (pay)
except:
	print ('Error. Please enter a numeric input!')	