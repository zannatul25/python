# ask user input in year and convert in days

# convert user input into integer
user_input = int(input("Enter integer number: "))

def year_to_days(year):
  day = 365 * year
  return day
result = year_to_days(user_input)
print(f"You are {result} days old")