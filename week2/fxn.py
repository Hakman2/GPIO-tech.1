#function: a block of reusable code to perform a particular tasks
# import time
# import math
# def cal_speed(distance, time):
#     speed = distance/time
#     return speed

# is_speed = cal_speed(2, 60 * 10)
# print(is_speed)


# print(cal_speed)

# def greeting(name):
#     print(f"Hello {name}")

# greeting('Olyvia')


# # area of a circle
# def areaOfCircle(radius):
#     area = math.pi * radius * radius
#     area = 22/7 * pow(radius,2)
#     # area = 22/7*radius**2
#     return area

# print(areaOfCircle(200))



# try:
#     takenum = int(input("Enter a positive number: "))
#     def is_even(takenum):

#         if takenum % 2 == 0:
#             print("true")
#         elif takenum % 2 != 0:
#             print("false")

#     is_even(takenum)

# except ValueError:
#     print("Please try again")

try:
    def is_true(takenum):
        result = takenum % 2 == 0
        return result

except NameError:
    print("sorry")
    import pandas as pd; 
