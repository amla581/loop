i=int(input('enter the num'))
num=i
sum=0
while i>0:
	sum=sum+(i%10)
	i=i//10
if num%sum==0:
	print(num,'harshad num')
else:
	print(num,'not harshad num')