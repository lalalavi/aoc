#!/usr/bin/env python
import sys


def main(fname):
    with open(fname) as fp:
        elves: str = fp.read()
        current_elf = 0
        list_elves = []
        for line in elves.splitlines():
            try:
                current_elf += int(line)
            except ValueError:
                list_elves.append(current_elf)
                current_elf = 0
    list_elves.sort(reverse=True)
    print(f"solution part1: {list_elves[0]}")
    print(f"solution part2 :D : {sum(list_elves[0:3])}")


if __name__ == "__main__":
    main(sys.argv[1])
