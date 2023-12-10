import sys
import re
import ipdb

def main(fname):
    with open(fname) as fp:
        lines = fp.read()
        min_loc, maps, current_map, seed_ranges  = 1 << 64, [], [], []
        part = 1
        for line in lines.splitlines()[2:]:
            if line != "":
                current_map.append(line)
            else:
                maps.append(current_map[1:])     #append without map name
                current_map = []
        for i, map in enumerate(maps):
            for j, entry in enumerate(map):
                maps[i][j] = entry.split(" ")
        if part == 1:
            seeds = re.findall(r'\d+', lines.splitlines()[0])
            for seed in seeds:
                eqv = int(seed)
                for map in maps:
                    for entry in map:
                        dest, source, length = int(entry[0]), int(entry[1]), int(entry[2]) 
                        if eqv >= source and eqv <= source+length:
                            eqv = dest + (eqv - source)
                            break
                min_loc = min(min_loc, eqv)
            print(f"solution1: {min_loc}")  
        else:
            seeds = re.findall(r'\d+', lines.splitlines()[0])
            for i in range(len(seeds)):
                if i % 2 == 0:
                    seed_ranges.append((int(seeds[i]), int(seeds[i])+int(seeds[i+1])))         
            loc_range_1 = (0, 1 << 64, 90)
            upper_bound = find_min_location(maps, seed_ranges, loc_range_1)
            print(f"found upper bound {upper_bound}")
            loc_range_2 = (0, upper_bound, 1)
            solution = find_min_location(maps, seed_ranges, loc_range_2)
            print(f"solution 2 - found location {solution} that corresponds to seed the seed range") 

def find_min_location(maps, seed_ranges, loc_range):
    for loc in range(*loc_range):
        eqv = loc
        for map in maps[::-1]:
            for entry in map:
                dest, source, length = int(entry[1]), int(entry[0]), int(entry[2])
                if eqv >= source and eqv <= source + length:
                    eqv = dest + (eqv - source)
                    break
        for seed_range in seed_ranges:
            if seed_range[0] <= eqv <= seed_range[1]:
                return loc
    return -1

if __name__ == "__main__":
    main(sys.argv[1])