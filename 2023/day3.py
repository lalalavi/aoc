import sys
import re

def main(fname):
    with open(fname) as fp:
        lines = fp.read().splitlines()
        mapping, adjacent_numbers = {}, {}
        gear_ratios =[]
        part = 2

        for idx,line in enumerate(lines): 
            for i,character in enumerate(line):   # for each character in the line, we create a mapping in a dictionary with its x,y coordinates where x is line number and y is index of character in line
                mapping[(idx,i)] = character       
        
        if part ==1:
            for key,value in mapping.items():  
                if value in ['%','!','*','-','@', '/', '#', '&', '$', '+', '^', '(', ')', '?', '>', '<', '=', ';', ':', '{', '}', '[', ']', '|', '~', '`', '\\']:
                    neighbours = get_neighbours(key)
                    for loc in neighbours:
                        if loc not in [item for sublist in adjacent_numbers.keys() for item in sublist]:
                            if mapping[loc].isnumeric():
                                current_digit, associated_locs = check_left_right(mapping[loc], loc, mapping, len(lines[0]))
                                adjacent_numbers[tuple(associated_locs)] = current_digit        # store the digit as value and the associated locations as the key because the key is unique, but the digits are not
                print(f"part1: {sum([int(value) for value in adjacent_numbers.values()])}")     # sum all digits (stored as keys in adjacent_numbers)
        
        if part==2:
            for key,value in mapping.items():  
                if value in ['*']:  
                    neighbours = get_neighbours(key)
                    adjacent_numbers[key] = []   # create a list for the digits associated with this special character
                    for loc in neighbours:
                        if mapping[loc].isnumeric():
                            digit, digit_loc = mapping[loc], loc
                            current_digit, associated_locs = check_left_right(digit, digit_loc, mapping, len(lines[0]))   
                            if current_digit not in adjacent_numbers[key]:                                 
                                # I introduce a limitation because this will fail if two equivalent digits are adjacent to the same special character
                                adjacent_numbers[key].append(current_digit)
            for key,value in adjacent_numbers.items():
                if len(value) == 2:
                    gear_ratios.append(int(value[0])*int(value[1]))
            print(f"part2: {sum(gear_ratios)}")
                            
def check_left_right(digit, digit_loc, mapping, len):
    '''
    Checks left and right to see if there are more digits
    '''
    original_digit_loc = digit_loc      # Store the original value of digit_loc to re-stablish later
    associated_locs = [original_digit_loc]
    while digit_loc[1]-1 >= 0 and mapping[(digit_loc[0],digit_loc[1]-1)].isnumeric():       # check left until we find a non-numeric character
        digit_loc = (digit_loc[0],digit_loc[1]-1)
        associated_locs.append(digit_loc)
        digit = mapping[digit_loc] + digit
    digit_loc = original_digit_loc     # reset digit_loc to original location
    while digit_loc[1]+1 < len and mapping[(digit_loc[0],digit_loc[1]+1)].isnumeric():      # check right until we find a non-numeric character
        digit_loc = (digit_loc[0],digit_loc[1]+1)
        associated_locs.append(digit_loc)
        digit = digit + mapping[digit_loc]
    return digit, associated_locs

def get_neighbours(key):
    x,y = key
    return [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]

if __name__ == "__main__":
    main(sys.argv[1])