n=int(input('enter the num'))
i=1
c=0
while i<=n:
	if n%i==0:
		c=c+1
	i=i+1
if c==2:
	print('prime num')
else:
	print('prime num nahi hai')


# def count_substring(string, sub_string):
#     count=0
#     for i in range(len(string)):
#         for j in range(len(sub_string)):
#             if string[i+j]==sub_string[j] and j==(len(sub_string)-1):
#                 count=count+1  
#             if string[i+j]!=sub_string[j]:
#                 break  
#         if i==len(string)-len(sub_string):
#             break            
#     return count


# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
    
#     count = count_substring(string, sub_string)
#     print(count)



# ourString = "Python Substring!"
# print(ourString[2])


# print(ourString[-1])


# print(ourString[1:6])


# print(ourString[:6])

# print(ourString[6:])

# # Get every second character between the index range of 0-6

# print(ourString[0:6:2])



# a='ABCDCDC'
# b='CDC'
# print(a.find(b))




# def split_and_join(line):
#     # write your code here
#     # String Split and Join in Python - HackerRank Solution START
#     Output = line.split()
#     Output = "-".join(Output)
#     return Output
#     # String Split and Join in Python - HackerRank Solution END
    
# if __name__ == '__main__':
#     line = input()
#     result = split_and_join(line)
#     print(result)



# a="1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2"
# storage = map(int, input().split())



# 