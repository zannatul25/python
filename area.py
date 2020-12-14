# user input 

radius = input("Enter radius: ")
radius = int(radius)
def area(r):
  a = 3.14 * (r ** 2)
  p = 2 * 3.14 * r
  return a, p

area, perimeter = area(radius)

print("The area of the surface: {0}".format(area))
print("The perimeter of the surface: {0}".format(perimeter))
