import sys
import re

def main(fname):
    with open(fname) as fp:
        lines = fp.read().splitlines()
        numbers_list = []
        # digitpair=contain_numberwords("twojkblghsctseven8eight","qdgdrtx9onefourdcvctldjnpcdjbc")    #testing edgecases
        for line in lines:
            digitpair = contain_numberwords(line)
            numbers_list.append(digitpair)
        print(f"solution: {sum(numbers_list)}")

def part1(line):
    n = re.findall(r'\d', line)   # find all single digits in string. reg \D for non digits
    if len(n) == 1:
        n= int(f"{n[0]}{n[0]}")   # when only one number, duplicate it
    else:
        n= int(f"{n[0]}{n[-1]}")  # concatenate the string digits and convert to int
    return n

def contain_numberwords(line):
    words = ["one","two","three","four","five","six","seven","eight","nine"]
    word_to_digit = {word: str(index + 1) for index, word in enumerate(words)}
    box = []

    for i,character in enumerate(line):
        if character.isdigit():
            box.append(character)
            continue  # Skip the word loop when a digit is found
        else:
            found = False
            for word in sorted(words, key=lambda x: line.find(x, i)):
                if line.startswith(word, i):
                    box.append(word_to_digit[word])
                    i += len(word)
                    found = True
                    break  # Stop searching for other words once one match is found
            if not found:
                i += 1     # If no word is found, move to the next character

    if len(box) == 1:
        box= int(f"{box[0]}{box[0]}")   # when only one number, duplicate it
    else:
        box= int(f"{box[0]}{box[-1]}")  # concatenate the string digits and convert to int

    return box

if __name__ == "__main__":
    main(sys.argv[1])
