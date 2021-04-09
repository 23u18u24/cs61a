from hog import *
from dice import make_test_dice
#
# dice = make_test_dice(3, 1, 5, 6)
# averaged_roll_dice = make_averaged(roll_dice, 1000)
# # Average of calling roll_dice 1000 times
# # Enter a float (e.g. 1.0) instead of an integer
# print(averaged_roll_dice(2, dice))

print(extra_turn_strategy(10, 19, cutoff=8, num_rolls=6))#0
print(extra_turn_strategy(30, 54, cutoff=7, num_rolls=6))#6
print(extra_turn_strategy(17, 36, cutoff=100, num_rolls=6))#0
print(extra_turn_strategy(24, 5, cutoff=1, num_rolls=6))#0


