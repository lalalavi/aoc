import sys
import math

def main(fname):
    with open(fname) as fp:
        lines = fp.read().splitlines()
        instruct = [0 if x == "L" else 1 for x in lines[0]]    
        tree = {}
        nodes_a = []

        for line in lines[2:]:  #Parse the network
            line = line.translate({ord(i): None for i in '() '}) #remove parentheses and spaces :)
            line = line.split("=")
            node, left, right = line[0], line[1].split(",")[0], line[1].split(",")[1]
            tree[node] = left, right
            if node.endswith("A"):
                nodes_a.append(node)

        steps = 0
        print(f"Nodes: {nodes_a}")
        steps_to_end = {n: 0 for n in nodes_a}
        
        for orig_node in nodes_a: #we will check for each node when does it reach any Z node and how many steps it takes
            steps = 0
            node = orig_node
            search = True
            while search: 
                for LR in instruct: 
                    if node.endswith("Z"):
                        steps_to_end[orig_node] = (steps, node)
                        search = False
                        break
                    node = tree[node][LR] 
                    steps += 1

        print(f"Solution: {math.lcm(*[x[0] for x in steps_to_end.values()])}")

if __name__ == "__main__":
    main(sys.argv[1])