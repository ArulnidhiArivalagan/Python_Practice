# #f-strings
# name="arulnidhi arivalagan"
# age=30
# height=1.6
# print(f"my name {name}i am{age}old")

#coding exercise

# n=int(input())
# years_left=90-n
# days_left=years_left*365
# months_left=years_left*12
# weeks_left=years_left*52

# print(f"you have{days_left} days,{months_left}months,{weeks_left}weeks")

# a=int(input())
# if(a%2==0):
#     print("even")
# else:                    #odd or even
#     print("odd")
  
# n=int(input())
# if(n>120 and n<=123):
#     print("Likely")
# else:
#     print("Unlikely")

# n=int(input())
# if(n%4==0):
#     if(n%100==0):
#         if(n%400==0):
#             print("leap")
#         else:
#             print("not leap year man")
#     else:
#         print("non leapyear")
# else:
#     print("nonleap")



#mulitple if else
n=int(input())
bill=0
if n<12:
    bill=150
    print("ticket price 159")
elif n<=18:
    bill=160
    print("ticket price 169")
else:
    bill=170
    print("ticket price is 500")
b=input("DO YOU WANT PHOTO Y/N?")
if b=='Y' or b=="N":
    bill=bill+50
    print(bill)
