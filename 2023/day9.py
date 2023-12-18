import sys
import numpy as np

def main(fname):
    with open(fname) as fp:
        lines = fp.read().splitlines()
        final_prediction = [0, 0]
        parts = [-1, 0]

        for i, part in enumerate(parts):
            for line in lines:  
                history = [int(x) for x in line.split()]
                Searching = True
                deltas = [history[i] - history[i-1] for i in range(1, len(history))]
                curr_delta_list = deltas
                last_deltas = [deltas[part]]

                while Searching:
                    if all(curr_delta_list[0] == delta for delta in curr_delta_list):
                        break
                    else:
                        curr_delta_list = [curr_delta_list[i] - curr_delta_list[i-1] for i in range(1, len(curr_delta_list))]
                        last_deltas.append(curr_delta_list[part])
            
                last_deltas.reverse()
              
                if part == -1:
                    last_deltas.insert(0, 0)
                    prediction = history[part] + np.cumsum(last_deltas)[part]
                else:
                    curr_difference = 0
                    for each in last_deltas:
                        difference = each - curr_difference
                        curr_difference = difference
                    prediction = history[part] - curr_difference
                
                final_prediction[i] += prediction
        
        print(f"solution p1 {final_prediction[0]} and p2 is {final_prediction[1]}")

if __name__ == "__main__":
    main(sys.argv[1])