from sys import argv

try:
	your_level = int(argv[1])
	your_skill = int(argv[2])
except IndexError:
	print("Call script with <your_level> <your_total_skill>")
	exit(1)

for i in range(1, 63):
	level_difference = int((your_level / 1.5 + your_skill / 3) - i)
	if level_difference >= 0:
		resist_chance = 10 - level_difference * 3
		resist_chance = max(resist_chance, 1)
	else:
		resist_chance = 10 + level_difference * level_difference * 3;
		resist_chance = min(resist_chance, 99)

	print('Chance you will get resisted ' + str(resist_chance) + ' for a level ' + str(i) + ' mob')
