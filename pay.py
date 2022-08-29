def pay (hour, rate):
	u = int (hour)
	w = int (rate)
	if u < 40:
		z = u * w
		print (z)
	if u >= 40:
		z = (((u - 40) * w * 1.5) + (w * 40))
		print (z)
	
t = input ('Enter the number of hours\n')
v = input ('Enter the rate\n')

pay(t,v)