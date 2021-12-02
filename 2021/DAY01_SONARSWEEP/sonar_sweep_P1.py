# Justin Ventura Advent of Code DAY 1

if __name__ == '__main__':
    lines = [line.rstrip('\n') for line in open('sonar_sweep_data.txt', 'r')]
    depths = list(map(int, lines))
    larger_than_prev = 0
    for i in range(1, len(depths)):
        if depths[i] > depths[i-1]:
            larger_than_prev += 1
    print(larger_than_prev)
