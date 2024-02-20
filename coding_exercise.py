# a=input("what kind of pizza u want (S/M/L)").lower()
# BILL=0
# if a=='S'or a=='s':
#     BILL+=200
#     print('amount is 200')
# elif a=='M' or a=='m':
#     BILL+=300
#     print('amount is 300')
# else:
#     BILL+=400
#     print('amonut is 400')
# add=input("do you want add anything(Y/N)?")
# if a=='Y':
#     BILL+=100
# else:
#     BILL+=5

# extra_chesse=input("DO YOU WANT EXTRA CHEESE(Y/N)?")
# if extra_chesse==" Y":
#     BILL+=20
# print(f"your final amount{BILL}")


# #Love calculator
# x=input("enter name1:")
# y=input("enter name2:")
# z=(x+y).lower()

# T=z.count('t')
# R=z.count('r')
# U=z.count('u')
# E=z.count('e')
# TRUE=T+R+U+E
# L=z.count('l')
# O=z.count('o')
# V=z.count('v')
# E=z.count('e')
# LOVE=L+O+V+E
# score=TRUE+LOVE

# print(score)


# coding exercise 3


# r1=[1,1,1]
# r2=[1,1,1]
# r3=[1,1,1]
# matrix=[r1,r2,r3]
# print(f"{r1}\n{r2}\n{r3}")
# a=input("enter the postition whre u hide money")

# row_number=int(a[0])
# column_number=int(a[1])
# row_selected=matrix[row_number-1]
# row_selected[column_number-1]='x'
# print(f"{r1}\n{r2}\n{r3}")


import random
user_choice=int(input("enter ur choice: type 0 for rock ,1 for stone,2 for scissors"))
c_choice=random.randint(0,2)
print("computer choice:")
print(c_choice)

if(c_choice == user_choice):
    print("DRAW")
elif(c_choice > user_choice):
    print('lose')
elif(user_choice > user_choice):
    print('win')
elif(c_choice == 0 and user_choice==2):
    print("u lose")
elif(user_choice==0 and c_choice==2):
    print("u win")