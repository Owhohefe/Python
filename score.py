try:
	num = input ('Enter a score between 0.0 and 1.0\n')
	score = float(num)
	if score < 0.0 or score > 1.0:
		print('Bad score!')
	else:
		if score >= 0.9:
			print ('You got an A!')
		elif score >= 0.8 and score < 0.9:
			print ('You got a B!')
		elif score >= 0.7 and score < 0.8:
			print ('You got a C!')
		elif score >= 0.6 and score < 0.7:
			print ('You got a D!')
		else:
			print ('You got an F!')
except:
	print('Bad Score!')