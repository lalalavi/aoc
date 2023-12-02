import sys
import re

def main(fname):
    with open(fname) as fp:
        lines = fp.read().splitlines()
        game_ids, game_powers = [],[]
        for i,line in enumerate(lines):
            game = solve(line)
            game_powers.append(game[1])
            if game[0]:                
                game_ids.append(i+1)
        print(f"solution part1 :D : {sum(game_ids)}")
        print(f"solution part2 :D : {sum(game_powers)}")

def solve(line):
    games = re.split(';|:', line)         # split by both comma and - to get limits of each range
    R,G,B = [],[],[]

    for round in games:
        rgb_data = round.split(",")
        for word in rgb_data:
            if "blue" in word:
                blue_digits = extract_digits(word)
                B.append(blue_digits)
            if "red" in word:
                red_digit = extract_digits(word)
                R.append(red_digit)
            if "green" in word:
                green_digits = extract_digits(word)
                G.append(green_digits)

    legal_game = (max(R)[0] <=12 and max(G)[0] <=13 and max(B)[0] <=14)
    power = max(R)[0]*max(G)[0]*max(B)[0]
    return legal_game, power

def extract_digits(word):
    n = re.findall(r'\d+', word)
    return [int(number) for number in n]

if __name__ == "__main__":
    main(sys.argv[1])
