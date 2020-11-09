from math import sqrt


def calculate_distance_from_center(x, y):
	d = sqrt((x ** 2) + (y ** 2))
	return d


def check_closest_point(point1, point2):
	x1, y1 = point1
	x2, y2 = point2
	distance_1 = calculate_distance_from_center(x1, y1)
	distance_2 = calculate_distance_from_center(x2, y2)
	if distance_1 <= distance_2:
		point1 = int(x1), int(y1)
		return point1
	else:
		point2 = int(x2), int(y2)
		return point2


first_point = (float(input()), float(input()))
second_point = (float(input()), float(input()))

print(check_closest_point(first_point, second_point))
