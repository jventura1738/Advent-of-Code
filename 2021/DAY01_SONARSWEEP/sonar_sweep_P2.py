# Justin Ventura Advent of Code DAY 1

if __name__ == '__main__':
    lines = [line.rstrip('\n') for line in open('sonar_sweep_data.txt', 'r')]
    depths = list(map(int, lines))
    larger_than_prev_sum = 0
    for i in range(0, len(depths)-3):
        first_window = sum(depths[i:i+3])
        second_window = sum(depths[i+1:i+4])
        if first_window < second_window:
            larger_than_prev_sum += 1
    print(larger_than_prev_sum)
