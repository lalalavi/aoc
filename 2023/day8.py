import sys
from collections import deque 

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
            # if A is in the last element of the node, add it to the list
            if node.endswith("A"):
                nodes_a.append(node)

        current_node = "AAA"
        steps = 0
        z_count = 0
        Searching = True   
        print(f"Nodes: {nodes_a}")
        # check = "".join([str(x) for x in instruct])
        # print(f"all inst: {check}")
        # print(f"Principal period: {principal_period(check)}")

       
        while Searching:
            for LR in instruct:
                for i, node in enumerate(nodes_a):    #evaluate exit condition
                    if node.endswith("Z"):
                        z_count += 1
                    if z_count == len(nodes_a) and node.endswith("Z"):
                        print(f"we reachedz biatchez yeyeyeyeyeeeee", nodes_a)
                        Searching = False
                        break
                if not Searching:
                    break
                z_count = 0
                steps += 1
                for i, node in enumerate(nodes_a):  
                    options = tree[node] #get the possibilities of the current node
                    if LR == 0:
                        nodes_a[i] = options[0]

                    else:
                        nodes_a[i] = options[1] 

        print(f"Solution: {steps}")

def principal_period(s):
    '''
    This is based on the observation that a string is periodic if and only if 
    it is equal to a nontrivial rotation of itself.'''
    i = (s+s).find(s, 1, -1)
    return None if i == -1 else s[:i]

if __name__ == "__main__":
    main(sys.argv[1])