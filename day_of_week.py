#Write a program that asks the user for a positive integer between 1 and 7(Assume that the user may enter any number from 1 to 7 both inclusive) and prints the day of week corresponding to that number in all capital letters. Assume that the day of the week starts from MONDAY. For example: if the user enters:

user_input = int(input("Enter number between 1 and 7: "))
def days_of_week(n):
  days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
  return days[n - 1]
result = days_of_week(user_input)
print(f"Today is {result}")
