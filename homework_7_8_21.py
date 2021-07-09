import math

#Has a function to calculate the square footage of a house
# Reminder  of formula : Length X Width == Area

#step 1
def house_area(width , length):
    area = width * length
    return area


width = float(input('Please enter the width of the house:'))
length = float(input('Please enter the length of the house: '))

total_area = house_area(width, length)

print(total_area)


#def h_a(w1, l1)
    #return w1 * l1

#ta = h_a(3, 3)

#print(ta)

# Has a function to calculate the circumference of a circle
two = 2.00
pi = math.pi
def circle_circum(two , pi , radius):
    circum = 2 * pi * radius
    return circum

radius = float(input('Please enter the radius of the circle:'))

total_circum = circle_circum(two, pi, radius)

print(circle_circum(two, pi, radius))

