height = int(input("Enter heght: "))

def main():
  pyramid(height)

def pyramid(h):
  for i in range(h):
    print(" " * (h - i - 1), end="")
    print("#" * (i + 1), end="")
    print("  ", end="")
    print("#" * (i + 1))


main()