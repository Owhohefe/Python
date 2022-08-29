total = 0
count = 0
z = 0
while True:
		x = input ('Enter a number\n')
		if x == 'done':
			break 
		try:	
			y = int (x) 
		except:
			print ('invalid entry')
			continue
		total = total + y
		count = count + 1
z = total/count
print (total)
print (count)
print (z)