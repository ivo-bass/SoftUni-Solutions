"""You are given the coordinates of four points in the 2D plane.
The first and the second pair of points form two different lines.
Print the longer line in format "(X1, Y1)(X2, Y2)" starting with the point
that is closer to the center of the coordinate system (0, 0).
If the lines are of equal length, print only the first one. """

from math import sqrt


def calculate_length(x1, y1, x2, y2):
	# diagonal of rectangle -> d*d = a*a + b*b
	length = sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2)
	return length


def check_longest_line(line1, line2):
	(x1, y1), (x2, y2) = line1
	(a1, b1), (a2, b2) = line2
	len_1 = calculate_length(x1, y1, x2, y2)
	len_2 = calculate_length(a1, b1, a2, b2)
	if len_1 >= len_2:
		return line1
	else:
		return line2


def calculate_distance_from_center(x, y):
	d = sqrt((abs(x) ** 2) + (abs(y) ** 2))
	return d


def check_closest_point(point1, point2):
	x1, y1 = point1
	x2, y2 = point2
	distance_1 = calculate_distance_from_center(x1, y1)
	distance_2 = calculate_distance_from_center(x2, y2)
	if distance_1 <= distance_2:
		return point1
	else:
		return point2


first_line = ((float(input()), float(input())), (float(input()), float(input())))
second_line = ((float(input()), float(input())), (float(input()), float(input())))

longer_line = check_longest_line(first_line, second_line)
first_point, second_point = longer_line
if second_point == check_closest_point(first_point, second_point):
	result = f"({int(second_point[0])}, {int(second_point[1])})({int(first_point[0])}, {int(first_point[1])})"
else:
	result = f"({int(first_point[0])}, {int(first_point[1])})({int(second_point[0])}, {int(second_point[1])})"

print(result)