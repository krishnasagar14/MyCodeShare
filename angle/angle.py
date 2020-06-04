def get_angle_between_hour_min_hands(hours, mins):
	"""
	Returns integer angle value between hour and minute hands.
	:param: hours: integer value between 0 to 12
	:param: mins: integer value between 0 to 60
	"""
	if not (0 <= hours <= 12):
		return
	if not (0 <= mins <= 60):
		return

	# If mins and hours are in permutations of edge values
	if mins in [0, 60] and hours not in [0, 12]:
		mins = 0
	elif mins == 0 and hours in [0, 12]:
		hours, mins = 0, 0

	# Edge case of 0, 60
	if hours == 0 and mins == 60:
		mins = 0

	# Finally: 0, 0 should lead to angle 0
	if mins == 0 and hours == 0:
		return 0

	angle_per_minute = 360 / 60
	angle_per_hour = 360 / 12

	delta_change_hours = (angle_per_hour * hours) + (angle_per_hour * (mins / 60.0))
	delta_change_mins = angle_per_minute * mins
	return abs(delta_change_hours - delta_change_mins)

print("Output")
print(get_angle_between_hour_min_hands(6, 30))
print(get_angle_between_hour_min_hands(12, 0))
print(get_angle_between_hour_min_hands(0, 60))
print(get_angle_between_hour_min_hands(0, 0))
print(get_angle_between_hour_min_hands(0, 3))
print(get_angle_between_hour_min_hands(3, 15))
print(get_angle_between_hour_min_hands(5, 0))
print(get_angle_between_hour_min_hands(5, 60))
print(get_angle_between_hour_min_hands(5, 30))
print(get_angle_between_hour_min_hands(5, 45))
print(get_angle_between_hour_min_hands(0, 15))
print(get_angle_between_hour_min_hands(8, 45))
print(get_angle_between_hour_min_hands(8, 23))
print(get_angle_between_hour_min_hands(7, 49))
print(get_angle_between_hour_min_hands(12, 39))
print(get_angle_between_hour_min_hands(13, 69))


# Output
# 15.0
# 0
# 0
# 0
# 16.5
# 7.5
# 150.0
# 150.0
# 15.0
# 97.5
# 82.5
# 7.5
# 113.5
# 59.5
# 145.5
# None