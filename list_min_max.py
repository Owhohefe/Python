z = []
while True:
	x = input ('Enter a number\n')
	if x == 'done':
		break
	try:
		y = int(x)
	except:
		print ('You must enter an integer number\n')
		exit()
	z.append(y)
print(z)
print (min(z))
print (max (z))