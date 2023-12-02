import sys


def main(fname):
    with open(fname) as fp:
        lines = fp.read().splitlines()

        stacks = []
        for _ in range(9):
            stacks.append([])
        #   stacks = [[] for _ in range(9) as a shorter version

        for line in lines[:8]:
            # print(line[5], line[25])
            # break
            for i in range(9):
                c = line[4*i + 1]  #read row as column
                print(c)
                if c != ' ':
                    stacks[i].append(c)
                    # print(f"Appending {c} to {stacks[i]} ")
        
        stacks = [x[::-1] for x in stacks]

        print(stacks)


if __name__ == "__main__":
    main(sys.argv[1])
