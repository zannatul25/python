#Write a program using while loop, which prints the sum of every third numbers from 1 to 1001 ( both 1 and 1001 are included)

#(1 + 4 + 7 + 10 + ....)
sum = 0
number = 1
while number <= 100:
  sum += number
  number += 3
print("Sum of every third numebr from 1 to 1001:", sum)