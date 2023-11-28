import sys
import string

def main(fname):
    part=2
    with open(fname) as fp:
        sacks = fp.read()
        list_priorities = []
        dict_values = {c: i for i,c in enumerate(string.ascii_letters, 1)} # assign a to z 1-26 and A-Z 27-52 by creating dict of values to map the stuff
        if part==1:
            for sack in sacks.splitlines():
                half1, half2 = sack[:len(sack)//2], sack[len(sack)//2:] #split in equal halves
                priority = ''.join(set(half1).intersection(half2)) #find letter intersecting in the two sets
                list_priorities.append(dict_values[priority])
            print(f"solution part1 :D : {sum(list_priorities)}")
        else:
            for sack_g in zip(*[iter(sacks.splitlines())]*3):
                priority = ''.join(set.intersection(*map(set,sack_g))) #find common character intersecting on all strings
                list_priorities.append(dict_values[priority])
            print(f"solution part2 :D : {sum(list_priorities)}")
        
if __name__ == "__main__":
    main(sys.argv[1])
