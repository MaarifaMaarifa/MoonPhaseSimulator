from matplotlib import pyplot as plt
from math import radians, sqrt, cos

time_period = 29.5
radius = 100


def turn_angle_finder(days_num):
    angle = (360 / time_period) * days_num
    if angle < 360:
        return angle
    else:
        return angle % 360


def dark_side_finder(angle):
    if angle < 180:
        return "left"
    else:
        return "right"


def terminus_side_finder(angle):
    if 0 < angle <= 90:
        return "right"
    elif 90 < angle <= 180:
        return "left"
    elif 180 < angle <= 270:
        return "right"
    elif 270 < angle <= 360:
        return "left"


def phase_teller(angle):
    if angle == 0 or angle == 360:
        return "New Moon"
    elif angle == 90:
        return "First Quarter"
    elif angle == 180:
        return "Full Moon"
    elif angle == 270:
        return "Last Quarter"
    elif 0 < angle < 90:
        return "Waxing Crescent"
    elif 90 < angle < 180:
        return "Waxing Gibbous"
    elif 180 < angle < 270:
        return "Waning Gibbous"
    elif 270 < angle < 360:
        return "Waning Crescent"


# A function for finding the x coordinates of the moon
def circle_x_generator(y, r):
    return sqrt(r ** 2 - y ** 2)


# A function for finding the x coordinates of the moon's terminus
def ellipse_x_generator(y, r, angle):
    radian_angle = radians(angle)
    return abs(r * cos(radian_angle) * sqrt(1 - (y / r) ** 2))


# Dealing with the moon(circle)
y = list(range(-radius, (radius + 1)))
circle_x_positive = []
circle_x_negative = []

for num in y:
    circle_x_positive.append(circle_x_generator(num, radius))
for num in circle_x_positive:
    circle_x_negative.append(-num)

plt.plot(y, circle_x_positive, color="black")
plt.plot(y, circle_x_negative, color="black")
plt.axis("square")

# Getting user input for the days and finding initial values
days = float(input("Enter the number of days since new moon: "))
turn_angle = turn_angle_finder(days)
terminus_side = terminus_side_finder(turn_angle)
dark_side = dark_side_finder(turn_angle)

# Dealing with the terminus(ellipse)
ellipse_x = []
if terminus_side == "right":
    for num in y:
        ellipse_x.append(ellipse_x_generator(num, radius, turn_angle))
elif terminus_side == "left":
    for num in y:
        ellipse_x.append(-ellipse_x_generator(num, radius, turn_angle))

print(ellipse_x)
print(terminus_side)
plt.plot(ellipse_x, y, color="black")

# Dealing with the moon shading(dark side)
if dark_side == "right":
    plt.fill_betweenx(y, circle_x_positive, ellipse_x, facecolor="grey")
elif dark_side == "left":
    plt.fill_betweenx(y, circle_x_negative, ellipse_x, facecolor="grey")

title = "Moon phase: " + phase_teller(turn_angle)
plt.title(title)
plt.show()
