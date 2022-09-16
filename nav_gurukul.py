i=1
while i<=50:
	if i%3==0:
		print(i,'nav')
	if i%7==0:
		print(i,'gurukul')
	if i%3==0 and i%7==0:
		print(i,'navgurukul')
	else:
		print(i)
	i=i+1