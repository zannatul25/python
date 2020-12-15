# 1. Write, in a file called mario.py in ~/pset6/mario/more/, a program that recreates these #half-pyramids using hashes (#) for blocks, exactly as you did in Problem Set 1, except that #your program this time should be written (a) in Python and (b) in CS50 IDE.
# 2. To make things more interesting, first prompt the user with get_int for the #half-pyramid’s height, a positive integer between 1 and 8, inclusive. (The height of the #half-pyramids pictured above happens to be 4, the width of each half-pyramid 4, with a gap #of size 2 separating them).
# 3. If the user fails to provide a positive integer no greater than 8, you should re-prompt #for the same again.
# Then, generate (with the help of print and one or more loops) the desired half-pyramids.
# Take care to align the bottom-left corner of your pyramid with the left-hand edge of your # terminal window, and ensure that there are two spaces between the two pyramids, and that # #there are no additional spaces after the last set of hashes on each row.

# main function

def main():
  pyramid()

#pyramid function
def pyramid():
  # to get positive integer between 1 and 8
  while True:
    try:
      height = int(input("Height: "))
      if height >= 1 and height <=8:
        break
    except ValueError:
      print("Enter number between 1 and 8")


  for i in range(height):
    print(" " * (height - i - 1), end="")
    print("#" * (i + 1), end="")
    print("  ", end="")
    print("#" * (i + 1))


main()