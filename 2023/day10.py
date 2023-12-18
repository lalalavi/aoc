import sys
import numpy as np

class Node:
    s: "Node"
    n: "Node"
    e: "Node"
    w: "Node"

N, E, S, W = 0, 1, 2, 3

def main(fname):
    with open(fname) as fp:
        lines = fp.read().splitlines()

        pos=None
        for y, line in enumerate(lines):
            for x, s in enumerate(line):
                if s == "S":
                    pos = 1
                    break
            if pos == 1:
                break
        
        if (s := lines[y-1][x]) in "F|7":
            y-=1
            dir = {"F": E, "|": N, "7": W}[s]
        elif (s := lines[y+1][x]) in "J|L":
            y += 1
            dir = {"J": W, "|": S, "L": E}[s]
        elif (s := lines[y][x-1]) in "F-L":
            x -= 1
            dir = {"F": S, "-": W, "L": N}[s]
        else:
            raise Exception("S does not connect on two points")
        cur_node = s
        steps = 1
        while cur_node != 'S':
            dir = {
                N: {"F": E, "|": N, "7": W},
                S: {"J": W, "|": S, "L": E},
                W: {"F": S, "-": W, "L": N},
                E: {"J": N, "7": S, "-": E},
            }[dir][cur_node]
            if dir == N:
                y-=1
            elif dir == S:
                y+=1
            elif dir == E:
                x+=1
            else:
                x-=1
            cur_node = lines[y][x]
         
            steps += 1
        
        print(steps / 2)



        


if __name__ == "__main__":
    main(sys.argv[1])