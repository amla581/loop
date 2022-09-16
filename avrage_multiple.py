num=int(input('enter the num'))
i=1
sum=0
while i<=num:
	weight=int(input('enter the num'))
	sum=sum+weight
	i=i+1
avrage=sum/num
if avrage%5==0:
	print('5 ka multiple hai',avrage)
else:
	print('5 ka multiple nahi hai',avrage)