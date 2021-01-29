                    ######### SPARE-PARTS #########

####################### MATH RELATED SOLUTIONS: ##########################


############ ODD OR EVEN:

def odd_or_even(arr):
    total = sum(arr)
    if total % 2 == 0:
        return "even"
    else:
        return "odd"


######## SQUARED SUM OF NUMBERS:
## squares each number that is passed in then returns the sum of array

def square_sum(numbers):
    return sum(x ** 2 for x in numbers)


######### SUM OF ALL NUMBERS BETWEEN TWO NUMBERS:
# Given two integers a and b, which can be positive or negative,
# find the sum of all the integers between including them too and
# return it. If the two numbers are equal return a or b.
# examples:   get_sum(1, 2) == 3   // 1 + 2 = 3

def get_sum(a,b):
    if a == b:
        return a
    if a < b:
        return sum(range(a,b +1))
    if a > b:
        return sum(range(b,a +1))



########## GET THE MEAN OF AN ARRAY:

from statistics import mean
import math
def get_average(marks):
    return math.floor(mean(marks))


###### CELSIUS CONVERTER:
## celsius = (fahrenheit - 32) * (5/9)

def weather_info (t):
    c = (t - 32) * (5.0 /9)
    return str(c) + " is freezing temperature" if c <= 0 else str(c) + " is above freezing temperature"


#### CHECK IF N IS DIVISIBLE BY X AND Y:

def is_divisible(n, x, y):
    if n % x == 0 and n % y == 0:
        return True
    else:
        return False


###### AREA OR PERIMETER: RECTANGLE OR SQUARE:
# You are given the length and width of a 4 - sided polygon.The polygon can either be a rectangle or a square.
# If it is a square, return its area. If it is a rectangle, return its perimeter.

def area_or_perimeter(l, w):
    if l == w:
        return l * w
    else:
        return (2 * l) + (2 * w)


#################### SPEED CONVERSION:
# Write a function which takes its speed in km per hour and
# returns it in cm per second, rounded down to the integer (= floored).

import math
def cockroach_speed(s):
    return math.floor(s*27.778)
#


######### FALLING SPEED OF PETALS: SPEED/DISTANCE CALCULATION:
# When it's spring Japanese cherries blossom, it's called "sakura" and it's admired a lot. Suppose that the
#  falling  speed of a petal is 5 centimeters per second(5 cm / s), and it takes 80 seconds for the petal
#  to reach the ground from a certain branch. Write a function that receives the speed( in cm / s) of a petal
#  as input, and returns the time it takes for that petal to reach the ground from the same branch.

def sakura_fall(v):
    return 400 / v if v > 0 else 0


#### CHECK IF NUMBER IS AUTOMORPHIC OR NOT:
# In mathematics, an automorphic number (sometimes referred to
# as a circular number) is a natural number in a given number base
#  whose square "ends" in the same digits as the number itself.

def automorphic(n):
    sqr = n ** 2
    x = len(str(n))
    last = sqr % pow(10, x)
    if last == n:
        return "Automorphic"

    else:
        return "Not"


######## FIND MULTIPLES OF A NUMBER:
# takes a value, integer , and returns a list of its multiples up to another value, limit .
# If limit is a multiple of integer, it should be included as well.
# For example, if the parameters passed are (2, 6), the function should
# return [2, 4, 6] as 2, 4, and 6 are the multiples of 2 up to 6.

find_multiples = lambda x,y: list(range(x,y+1,x))



######## PONY EXPRESS:
# stations is a list/array of distances (miles)
# from one station to the next along the Pony Express route.
# Implement the riders method/function, to return how many riders are
# necessary to get the mail from one end to the other.
# NOTE: Each rider travels as far as he can, but never more than 100 miles.

def riders(stations):
    riders, rode = 1, 0
    for distance in stations:
        if rode + distance > 100:
            riders +=1
            rode = distance
        else:
            rode += distance
    return riders


###### DRY POTATOES PERCENTAGES/WEIGHTS/CONVERSIONS:
# All we eat is water and dry matter.
# John bought potatoes: their weight is 100 kilograms.
# Potatoes contain water and dry matter.
# The water content is 99 percent of the total weight. He thinks
# they are too wet and puts them in an oven - at low temperature -
# for them to lose some water.
# At the output the water content is only 98%.
# What is the total weight in kilograms (water content plus dry matter)
# coming out of the oven?

def potatoes(p0, w0, p1):
    x = (100-p0) * w0
    return int(x/(100-p1))


######## FIND SMALLEST UNUSED ID NUMBER:

def next_id(arr):
    for i in range(0, len(arr)+1):
        if not i in arr:
            return i


########### CHECK IF CAN WE DIVIDE IT:
# check if an integer number is divisible by each of two arguments

def is_divide_by(number, a, b):
    if number % a == 0 and number % b == 0:
        return True
    else:
        return False

