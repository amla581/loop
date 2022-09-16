num=int(input('enter the num'))
count=0
i=1
while i<=num:
	if num%i==0:
		count+=1
	i=i+1
if count==2:
	print(num,'prime num hai')
else:
	print(num,'prime num nahi hai')