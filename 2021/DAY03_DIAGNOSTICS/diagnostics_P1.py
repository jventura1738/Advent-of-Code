# Justin Ventura Advent of Code DAY 3

from functools import reduce
import operator


def get_gamma_epsilon_rates(binary_map):
    gamma_rate_bin = list()
    epsilon_rate_bin = list()
    for column in binary_map.values():
        gamma_rate_bin.append(max(set(column), key=column.count))
        epsilon_rate_bin.append(min(set(column), key=column.count))

    gamma_rate_bin, epsilon_rate_bin = ''.join(
        gamma_rate_bin), ''.join(epsilon_rate_bin)
    return int(gamma_rate_bin, 2), int(epsilon_rate_bin, 2)


if __name__ == '__main__':
    diagnostics = [line.rstrip() for line in open('diagnostics.txt', 'r')]
    binary_code_length = len(diagnostics[0])
    binary_mapping = {k: list() for k in range(binary_code_length)}
    for binary_code in diagnostics:
        for i, character in enumerate(binary_code):
            binary_mapping[i] += [character]

    power_consumption = reduce(
        operator.mul, get_gamma_epsilon_rates(binary_mapping))
    print(power_consumption)
