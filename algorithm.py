import numpy as np
import math

def algorithm(cities,start_point,i_start):

	order = [i_start]
	length = 0
	next_city = start_point
	while len(order) < cities.shape[0]:
		i_next, next_city, dist = get_closest(next_city, cities, order)
		length += dist
		order.append(i_next)
			
	return order, length

def get_closest(city, cities, visited):
	best_distance = float('inf')

	for i, c in enumerate(cities):
		if i not in visited:
			
			distance = dist(city, c)

			if distance < best_distance:
				closest_city = c
				i_closest_city = i
				best_distance = distance

	return i_closest_city, closest_city, best_distance

def dist(c1, c2):
	R = 6373
	lat1 = math.radians(c1[0])
	lon1 = math.radians(c1[1])

	lat2 = math.radians(c2[0])
	lon2 = math.radians(c2[1])

	dlon = lon2 - lon1
	dlat = lat2 - lat1
	a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
	c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

	return R * c