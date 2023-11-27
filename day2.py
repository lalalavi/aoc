#pppooopie
import sys

def main(fname):
    with open(fname) as fp:
        pairs= fp.read()
        list_rounds = []
        for pair in pairs.splitlines():
            pair = pair.replace(" ", "")         
            outcome_pair = calculate_outcome(pair)
            list_rounds.append(outcome_pair)
        total_score = sum(list_rounds)
        print("Total Score:", total_score)
    
def calculate_outcome(pair):
    shape_dict = {
        "AZ": 0+3, "AY": 6+2, "AX": 3+1,
        "BX": 0+1, "BZ": 6+3, "BY": 3+2,
        "CY": 0+2, "CX": 6+1, "CZ": 3+3
    }
    shape_dict_p2 = {
        "AZ": 2+6, "AY": 1+3, "AX": 3+0,
        "BX": 1+0, "BZ": 3+6, "BY": 2+3,
        "CY": 3+3, "CX": 2+0, "CZ": 1+6
    }
    if pair in shape_dict_p2:
        return shape_dict_p2[pair]

if __name__ == "__main__":
    main(sys.argv[1])






