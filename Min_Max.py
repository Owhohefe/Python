largest = None
smallest = None
while True:
		x = input ('Enter a number\n')
		if x == 'done':
			break 
		try:	
			y = int (x) 
		except:
			print ('invalid entry')
			continue
		if smallest is None or y < smallest :
			smallest = y
		if largest is None or y > largest :
			largest = y
print (smallest)
print (largest)