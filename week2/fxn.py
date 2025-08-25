#function: a block of reusable code to perform a particular tasks
import time
import math
def cal_speed(distance, time):
    speed = distance/time
    return speed

is_speed = cal_speed(2, 60 * 10)
print(is_speed)


# print(cal_speed)

def greeting(name):
    print(f"Hello {name}")

greeting('Olyvia')


# area of a circle
def areaOfCircle(radius):
    area = 22/7 * pow(radius,2)
    # area = 22/7*radius**2
    return area

print(areaOfCircle(200))
