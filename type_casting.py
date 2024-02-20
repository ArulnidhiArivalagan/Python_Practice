# # print(len("arulnidhi"))

# # a=len("arulnidhiarivalagan")
# # print(type(a))
# # # print("ur name"+ str(a)+ "character")

# # print(10+float("10"))

# # name="arul"
# # print(10+str(name))

# # a=int(input())
# # b=int(input())
# # c=a+b
# # print(c)



# #all loops are in python

# x=["python","sql","java"] #for loop example  
# for i in x:
#     print(i)

# a=1
# while a<3:      #while loop
#     print(a)
#     a=a+1

# y=["leetcode","codechef"]
# num=[1,2]               #nested loop 
# for i in y:
#     for j in num:
#         print(i,j)
    
# b=2
# if b==7:
#     print("value is 7")
# elif b==2:                  #elif if statetement 
#     print("value is 2")
# else:
#     print("value is none")

# Python3 code to find largest three
# elements in an array
import sys
def printlargest(arr, arr_size):

	if (arr_size < 3):
	
		print(" Invalid Input ")
		return
	
	third = first = second = -sys.maxsize
	
	for i in range(0, arr_size):

		if (arr[i] > first):
		
			third = second
			second = first
			first = arr[i]
	
		elif (arr[i] > second):
		
			third = second
			second = arr[i]
		
		elif (arr[i] > third):
			third = arr[i]
	
	print("Three largest elements are",
				first, second, third)
arr = [12, 13, 1, 10, 34, 1]
n = len(arr)
printlargest(arr, n)


