from sys import stdin


def roll_x_dice(dice):
    return [dice[2], dice[1], dice[5], dice[3], dice[0], dice[4]]


def roll_y_dice(dice):
    return [dice[1], dice[5], dice[2], dice[0], dice[4], dice[3]]


def roll_dice(dice, tries=0):
    if tries < 3:
        return roll_x_dice(dice)
    elif tries == 3:
        dice = roll_x_dice(dice)
        return roll_y_dice(dice)
    return roll_y_dice(dice)


def maximum_side_of_dice(dice):
    return max(dice[1:5])


def get_top_of_dice(dice):
    return dice[0]


def get_bottom_of_dice(dice):
    return dice[5]


num_of_dice = int(stdin.readline())
dices = [
        [int(val) for val in stdin.readline().split()]
        for _ in range(num_of_dice)
        ]
first_dice = dices[0]
rest_dices = dices[1:]

maximum_side_of_dice_tower = 0
for i in range(8):
    print('first_dice: ' + str(first_dice))
    current_maximum_side_of_dice_tower = 0
    top = get_top_of_dice(first_dice)
    for dice in rest_dices:
        print(dice)
        for j in range(8):
            if get_bottom_of_dice(dice) == top:
                break
            dice = roll_dice(dice, j)
            print(dice)

        print('end')

        top = get_top_of_dice(dice)
        current_maximum_side_of_dice_tower += maximum_side_of_dice(dice)

    print(current_maximum_side_of_dice_tower)
    if current_maximum_side_of_dice_tower > maximum_side_of_dice_tower:
        maximum_side_of_dice_tower = current_maximum_side_of_dice_tower

    first_dice = roll_dice(first_dice, i)

print(maximum_side_of_dice_tower)
