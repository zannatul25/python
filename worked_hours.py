#Write a program which asks the user to enter an integer 'n' which would be the total numbers of hours the user worked in a week and calculates and prints the total amount of money the user made during that week. If the user enters any number less than 0 or greater than 168 (n < 0 or n > 168) then your program should print INVALID

#Assume that hourly rate for the first 40 hours is $8 per hour.
#Hourly rate for extra hours between 41 and 50 (41 <= n <= 50 ) is $9 per hour.
#Hourly rate for extra hours greater than 50 is $10 per hour.
#Here are a few examples:
# if the user enters -5, then your program should print "INVALID"
# if the user enters 34, then your program should print "YOU MADE 272 DOLLARS THIS WEEK"
# if the user enters 45, then your program should print "YOU MADE 365 DOLLARS THIS WEEK"
# if the user enters 67, then your program should print "YOU MADE 580 DOLLARS THIS WEEK"

user_input = int(input("Enter hours in a week: "))
def worked_hours(n):
  total_pay = 0

  if n < 0 or n > 168:
      return "INVALID"
  elif n <= 40:
      total_pay += n * 8 
      return "YOU MADE {0} DOLLARS THIS WEEK".format(total_pay)
  elif n <= 50:
      total_pay += 40 * 8 + (n - 40) * 9
      return "YOU MADE {0} DOLLARS THIS WEEK".format(total_pay)
  else:
      total_pay += 40 * 8 + 10 * 9 + (n - 50) * 10
      return "YOU MADE {0} DOLLARS THIS WEEK".format(total_pay)
  

result = worked_hours(user_input)
print(result)
