# num1=int(input('enter the num'))
# num2=int(input('enter the num'))
# if num1>num2:
# 	a=num1
# else:
# 	a=num2
# while num1>0:
# 	if (a%num1==0 and a%num2==0):
# 		lcm=a
# 		break
# 	a=a+1
# print('lcm is',lcm)

# a=int(input("enter the num"))
# b=int(input("enter the num"))
# i=1
# while i<=10:
# 	print(a*i,b*i)
# 	i=i+1
n=int(input("enter the num"))
c=0
for i in range(2,n):
	if n%i==0:
		c+=1
		# break
	if c==2:
		print("prime")
	else:
		print("not prime")