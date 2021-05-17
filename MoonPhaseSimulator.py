from matplotlib import pyplot as plt
from math import sqrt, sin, radians

###     A function for generating the y coordinates for the moon   ###
def circle_y_generator(x):
    if (400-x**2) > 0 or (400-x**2) == 0:
        return sqrt(400-x**2)

###     A function for generating the x coordinates for the terminator which is an ellipse  ###
def ellipse_x_generator(y,t):
    return 20 * sin(radians(90-(360*t)/27.9)) * sqrt(1-(y**2/400))


circle_x_coordinates = list(range(-20,21))
circle_y_positive_coordinates = []
circle_y_negative_coordinates = []
ellipse_x = []

for num in circle_x_coordinates:
    circle_y_positive_coordinates.append(circle_y_generator(num))

for num in circle_y_positive_coordinates:
    circle_y_negative_coordinates.append(0-num)

###     A plot for the moon    ###
plt.plot(circle_x_coordinates,circle_y_positive_coordinates, color="blue")
plt.plot(circle_x_coordinates,circle_y_negative_coordinates, color="blue")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("The Moon")

ellipse_x_coordinates = []

days = float(input("Enter the number of days since new moon: "))
for num in circle_y_positive_coordinates:
    ellipse_x_coordinates.append(ellipse_x_generator(num,days))

###       A plot for the moon's terminator     ###
plt.plot(ellipse_x_coordinates, circle_y_positive_coordinates, color="green")
plt.plot(ellipse_x_coordinates, circle_y_negative_coordinates, color="green")
plt.show()
