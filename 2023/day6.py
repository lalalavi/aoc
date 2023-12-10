import sys
import re

def main(fname):
    with open(fname) as fp:
        lines = fp.read().splitlines()
        part2 = True
        times = [int(x) for x in lines[0].split(':')[1].split()]
        dists = [int(x) for x in lines[1].split(':')[1].split()]
        if part2 == True:
            times = [int(''.join(map(str, times)))]    #take all elements in list and concatenate them into a single number
            dists = [int(''.join(map(str, dists)))]
        sol =  1
        for t,dist in zip(times, dists):
            wins = 0
            for holding in range(1,t):
                if (t - holding) * holding > dist:
                    wins += 1
            print(f"wins of race of zip combination {t} and {dist} is {wins}")
            p1 *= wins
        print(f"Solution: {sol}")
           
if __name__ == "__main__":
    main(sys.argv[1])