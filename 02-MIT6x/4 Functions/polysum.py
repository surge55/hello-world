################################################################################
## Course: MITx 6.001x - Intro to CS and Programming Using Python
## Student: surge
## Date: June 17, 2022
## Exercise: polysum
'''
A regular polygon has n number of sides. Each side has length s.
The area of a regular polygon is: 0.25*n*s^2 / tan(pi/n)
The perimeter of a polygon is: length of the boundary of the polygon
Write a function called polysum that takes 2 arguments, n and s. This function should 
sum the area and square of the perimeter of the regular polygon. The function returns 
the sum, rounded to 4 decimal places.
'''
################################################################################

import math
def polysum(n, s):
    '''

    :param n: an integer, number of sides
    :param s: an integer, length of each side
    :return: sum of the area of a regular polygon and the square of its perimeter. Rounded to 4 decimal places.
    '''

    area = 0.25*n*s**2 / math.tan(math.pi/n)

    perimeter = (n*s)**2

    return round(area + perimeter, 4)

# print(polysum(60,83))

