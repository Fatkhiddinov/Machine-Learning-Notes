import random

doors = ["Goat","Car","Goat"]

win_stay = 0
win_change = 0
iter = 1000000

for i in range(iter):
  random.shuffle(doors)
  first_guess = random.choice(doors)

  if first_guess == "Car":  # if it's a car, the decision to stay will win.
    win_stay += 1
  else:                     # if not, monty opens another goat door and decision to change will win.
    win_change += 1

print("Win rate (don\'t change): ", win_stay/iter*100)
print("Win rate (changed doors): ", win_change/iter*100)
