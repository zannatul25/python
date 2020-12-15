#Write a program that asks the user to enter a positive integer n. Assuming that this integer is in seconds, your program should convert the number of seconds into days, hours, minutes, and seconds and prints them exactly in the format specified below. Here are a few sample runs of what your program is supposed to do:
# when user enters "369121517" your program should print: "4272 days 5 hours 45 minutes 17 seconds"
# when user enters "24680" your program should print: "0 days 6 hours 51 minutes 20 seconds"
# when user enters "129600" your program should print: "1 days 12 hours 0 minutes 0 seconds"

user_input = input("Enter positive integer: ")
number_in_second = int(user_input)
def get_days(n):

  days = n // (24 * 60 * 60)
  # remaining seconds after we get days
  remain_second = n % (24 * 60 * 60)
  hours = remain_second // (60 * 60)
  # remaining seconds after we get hours
  remain_second = remain_second % (60 * 60)
  mins = remain_second // 60
  # remaining seconds after we get minutes
  seconds = remain_second % 60
  return f"{days} days {hours} hours {mins} minutes {seconds} seconds"

result = get_days(number_in_second)
print(result)