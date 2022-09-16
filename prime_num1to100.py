i=1
while i<=100:
	p=0
	j=1
	while j<=i:
		if i%j==0:
			p=p+1
		j=j+1
	if p==2:
		print(i)
	i=i+1
# dic={"a":4,"b":4,"c":7}
# d={}
# for i in dic:
# 	# for j in dic:
# 	if False:
# 		s=dic[i]+dic[i+1]
# 		d[i]=s
# 			# print(d)
# 	else:
# 		d[i]=dic[i]
# 	print(d)

