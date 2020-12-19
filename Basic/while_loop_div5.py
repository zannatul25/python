#Write a program which prints the sum of numbers from 1 to 101 that are divisible by 5. ( 1 and 101 are included) (Use while loop)
number = 1
sum = 0
while number <= 101:
  if number % 5 == 0:
    sum += number
    print("number:", number)
  number += 1
print(sum)