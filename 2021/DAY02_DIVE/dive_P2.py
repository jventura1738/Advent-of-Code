# Justin Ventura Advent of Code DAY 2
from typing import Tuple


def shift_position(direction: str, magnitude: int) -> Tuple[int]:
    if direction == 'forward':
        return 0, magnitude
    elif direction == 'down':
        return magnitude, 0
    elif direction == 'up':
        return -magnitude, 0


if __name__ == '__main__':
    course = [line.rstrip() for line in open('dive.txt', 'r')]
    curr_depth = 0
    curr_horizontal = 0
    curr_aim = 0
    for command in course:
        direction, magnitude = command.split()
        aim_delta, magnitude_delta = shift_position(
            direction, int(magnitude))
        curr_aim += aim_delta
        curr_horizontal += magnitude_delta
        curr_depth += curr_aim * magnitude_delta

    print(curr_depth * curr_horizontal)
