n=int(input('enter the num'))
s=n
while s>=10:
	div=s 
	s=0
	while div>0:
		s=s+(div%10)
		div=div//10
if s==1:
	print('happy num hai',n)
else:
	print('happy num nahi hai',n)

