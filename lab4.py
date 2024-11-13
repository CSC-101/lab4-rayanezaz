import data
import math

# Write your functions for each part in the space below.

# Part 1

#The purpose of this function is return a list with the first element of each nested list from
#the input (which is a nested list of list[list[int]]. Additionally, it looks for empty lists and will not return anything from that nested
#list. The input is lists within lists written as ints, and the output is a list
def first_element(vals: list[list[int]])-> list:
    listOne = []
    for x in range(len(vals)):
        if len(vals[x]) > 0:
            listOne.append(vals[x][0])
    return listOne

# Part 2

#The purpose of this function is to return a list with the x-coordinate of each point when the
#input is a list of list[data.Point]. The input is a list of ints, and the output is also a list of ints.
def x_coordinates(vals: list[data.Point])-> list:
    listOne = []
    for a in vals:
        listOne.append(a.x)
    return listOne

# Part 3

#The purpose of this function is to return all points from the input list in the first quadrant
#of a plane when the input is a list[data.Point]. So, the input is a list of ints (list[int]) and
#the output is also a list of ints (list[int])
def are_in_positive_quadrant(vals: list[data.Point])->list[list]:
    listOne = []
    for a in vals:
        if a.x > 0 and a.y > 0:
            listOne.append([a.x, a.y])
    return listOne

# Part 4

#The purpose of this function is to return the Euclidean distance between two points.
#The return must be of type float, and this happens when the function is given two
#parameters of type Point (data.Point). The input is of type float and the output is
#also of type float
def distance(vals1: data.Point, vals2: data.Point)->float:
    eucl_dist = math.sqrt((vals2.x - vals1.x)**2 + (vals2.y - vals1.y) **2)
    return eucl_dist

# Part 5

#The purpose of this function is to return the Manhattan distance between two points.
#The return must be of type float, and this happens when the function is given two
#parameters of type Point (data.Point). The input is of type float and the output is
#also of type float
def manhattan_distance(vals1: data.Point, vals2: data.Point)->float:
    manh_length = abs(vals1.x - vals2.x) + abs(vals1.y - vals2.y)
    return manh_length

# Part 6

#The purpose of this function is to return a list with the distance between the origin
#and given points in the list. So, this can be achieved when the function is given a
#list of points/ints (list[data.Point]. The input is of type list with ints and the output
#is also of type list of ints.
def distance_all(vals: list[data.Point])->float:
    for a in range(len(vals)):
        distance_records = (math.sqrt((vals[a].x-0)**2+(vals[a].y-0)**2))
    return float(round(distance_records, 2))

