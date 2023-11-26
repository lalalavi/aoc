#pppooopie
import sys

def main(fname):
    with open(fname) as fp:
        pairs= fp.read()
        list_rounds = []
        for pair in pairs.splitlines():
            a = pair.split()[0]
            b = pair.split()[1]
            outcome_pair = calculate_outcome(a,b)
            #update  with the shape chosen - another function
            #append to result list of rounds
        #sum all over the mfkin list, then return the total score
 
def calculate_outcome(o, c):
    if (o == "A" and c == "Z") or (o == "B" and c == "X") or (o == "C" and c == "Y"):
        print('ya losing son')
        return 0
    if (o == 'A' and c == 'Y') or (o == 'B' and c == 'Z') or (o == 'C' and c == 'X'):
        print('ya winning son')
        return 6  
    else:
        print('ya tie')
        return 3  
    
def calculate_shape(chosen_shape):
    shape_dict = {
        "Y": 2,  #Paper
        "X": 1,  #Rock
        "Z": 3  #Scissors
    }

'''
    outcome_dict = {
        "A": ["Z", "Y"], # you lose, opp loses
        "B": ["X", "Z"], # you lose
        "C": ["Y", "X"]  # you lose
    }    
'''

if __name__ == "__main__":
    main(sys.argv[1])






