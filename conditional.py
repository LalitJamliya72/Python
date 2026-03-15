# age = 24
# if age>=18:
#     print("you are eligible for vote")
# else:
#     print("you are a minor")

year = int(input("enter the year:"))
if year%4==0:
    if year%100==0:
     if year%400==0:
       print(year, "is a leap year")
    else:
     print(year, " is not a leap year")          
else:
 print(year, "is a leap year")   