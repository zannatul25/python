#Write a program using while loop, which asks the user to type a positive integer, n, and then prints the factorial of n. A factorial is defined as the product of all the numbers from 1 to n (1 and n inclusive). For example factorial of 4 is equal to 24. (because 1*2*3*4=24)
user_input = input("Enter positive number: ")
number = int(user_input)
def get_fact(n):
  fact = 1
  while n > 0:
    fact *= n
    n -= 1
  return fact
result = get_fact(number)
print(f"{number}! = {result}")