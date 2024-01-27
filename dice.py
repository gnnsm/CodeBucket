import re
import random


def calculate(number, dice_cube, append):
    result = 0
    while number > 0:
        throwing = random.randint(1, dice_cube)
        result += throwing
        # print(f'Dice #{number}: {throwing}')
        number -= 1
    result += append
    return result


def dice(command: str):
    append = 0
    command = re.sub('\s+', '', command).lower()
    if not bool(re.match(r'^(\d+)?d\d+(\+\d+)?$$', command)):
        return ':angry:'
    else:
        split_append = re.split(r'\+', command)
        if len(split_append) != 1:
            append = int(split_append[-1])
        split_d = re.split(r'd', split_append[0])
        if len(split_d[0]) == 0:
            number = 1
        else:
            number = int(split_d[0])
        die = int(split_d[1])
        return calculate(number, dice_cube, append)


if __name__ == "__main__":
    print(dice('2d6+5'))
