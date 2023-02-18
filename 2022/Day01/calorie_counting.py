import heapq


"""
P1: Find the elf with the highest total calorie count.
P2: Find the elves with the highest three total calorie counts.

Note: could be done in O(n) time and O(1) space by keeping track of the
three largest values as we go through the input file, but for this AoC
I wanted to practice for interviews (readability, modularity, etc.).
"""


# O(n) time, O(n) space where n is the number of lines in the input file
def get_input() -> list:
    with open("input1.txt", "r") as f_in:
        elves = []
        elf, calories = 0, 0
        for line in f_in:
            # Empty lines separate elves:
            if line == "\n":
                elves.append(calories)
                elf, calories = elf + 1, 0
                continue

            calories += int(line)
        return elves


if __name__ == "__main__":
    elf_caloric_totals = get_input()
    largest_total = max(elf_caloric_totals)  # O(n) time
    largest_three = sum(heapq.nlargest(
        n=3, iterable=elf_caloric_totals))  # O(n log n) time
    print("P1 solution:", largest_total)
    print("P2 solution:", largest_three)
