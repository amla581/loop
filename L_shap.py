r=0
while r<=4:
	c=0
	while c<=4:
		if c==0 or r==4:
			print('*',end=' ')
		else:
			print(' ',end=' ')
		c+=1
	print()
	r+=1