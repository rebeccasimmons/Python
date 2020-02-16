#######################################################
# Program: Obtaining month day and year in numerical  #
# Description: Obtain m, d, y in numerical and        #
#     asking user if they want to continue the program#
# Author: Rebecca Hope Simmons                        #
# Date: Wednesday, October 1, 2014                    #
#######################################################

# while loop 

date = "yes"
while date == "yes": 

   # Evaluate the	month	, day	, and	year
   month, day,	year = eval(input("Enter month day year with commas: "))
   
   # Determine	the month
   if	month	==	1:	
   	monthName = "January"
   elif month == 2:
   	monthName = "February"
   elif month == 3:
   	monthName = "March"
   elif month == 4:
   	monthName = "April"
   elif month == 5: 
   	monthName = "May"
   elif month == 6:
   	monthName = "June"
   elif month == 7:
   	monthName = "July"
   elif month == 8:
   	monthName = "August"
   elif month == 9:
   	monthName = "September"
   elif month == 10:
   	monthName = "October"
   elif month == 11:
   	monthName = "November"
   elif month == 12:
   	monthName = "December"
   else:
   	print("Invalid Month")
      
   # if month and	day IS valid 
   if	(month == 1	or	month	==	3 or month == 5 or month == 7	or	month	==	8 or month == 10 or month == 12):
      if day <= 31 and day	>=	1:
         print(monthName, day, year)# print date, valid or invalid
      else:
         print("Invalid Day")
   elif (month	==	4 or month == 6 or month == 9	or	month	==	11):
   	if	day <= 30 and day	>=	1:
         print(monthName, day, year)# print date, valid or invalid
   	else:
         print("Invalid Day")
   elif (month	==	2):
      if	day <= 28 and day	>=	1:
   	   print(monthName, day, year)# print date, valid or invalid
      else:
         print("Invalid Day") 
   else:
      print("Invalid Day")

   date = input("Do you want to continue?") 
   
print("Goodbye!")

   
   

 
