import sys
import re

def main(fname):
    with open(fname) as fp:
        lines = fp.read().splitlines()
        total_score = 0
        count_list = []
        for _ ,line in enumerate(lines):
            count = find_winning(line)
            count_list.append(count)
            card_score = 0
            if count >1:
                card_score = 2**(count-1)
                total_score += card_score
            else:
                card_score = count
                total_score += card_score
       
        copies = [1] * len(count_list)   # one copy of each card as the beginning state. Creates a list of 1s
        for i, count_value in enumerate(count_list):
            for j in range(i + 1, i + count_value + 1):
                copies[j] += copies[i] 
                #print(f'Adding {copies[i]} copies to card {j+1} because there are {count_value} matches in card {i+1}')
                
        print(f'sol part1 {total_score}')
        print(f'sol part2 {sum(copies)} copies {copies}')            

    
def find_winning(line):
    _, numbers = line.split(':')
    numbers = numbers.split('|')
    winning_n, exist_n = numbers[0], numbers[1]
    winning_n = re.findall(r'\d+', winning_n)
    exist_n = re.findall(r'\d+', exist_n)
    count = 0               #count the number of matches between winning and existing numbers
    for n in winning_n:     #alternatively, use set intersection (!!!!) more efficient
        if n in exist_n:
            count += 1
    return count

if __name__ == "__main__":
    main(sys.argv[1])