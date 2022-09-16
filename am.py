a=int(input('enter the num'))
i=1
s=0
while i<=a:
	s=s+(a%10)
	a=a//1000
print(s)


