def computegrade(score):
	try:
		x = float (score)
		if x < 0.0 or x >= 1.0:
			print ('Bad score')
		else:
			if x >= 0.9:
				print ('A')
			elif x >= 0.8 and x < 0.9:
				print ('B')	
			elif x >= 0.7 and x < 0.8:
				print ('C')	
			elif x >= 0.6 and x < 0.7:
				print ('D')	
			else:
				print ('F')	
	except:
		print('you must enter an integer')
			
y = input('Enter a score between 0.0 and 0.1\n')

computegrade(y)