import sys
import re

def main(fname):
    with open(fname) as fp:
        pairs = fp.read()
        results = []
        for pair in pairs.splitlines():
            range_limits = re.split('-|,', pair)         # split by both comma and - to get limits of each range
            r1 = range(int(range_limits[0]), int(range_limits[1]))
            r2 = range(int(range_limits[2]), int(range_limits[3])) 
            sol = checkrange(r1,r2)
            results.append(sol)
        print(f"Total Completely Contained: {sum(result[0] for result in results)}")
        print(f"Total Overlapping: {sum(result[1] for result in results)}")
        
def checkrange(r1,r2):
    '''
    1st if checks if any of the input is completely contained by the other one
    2nd if statement checks for overlap of ranges.
    Returns a tuple of booleans for maxxxxximum efficiency :D
    '''
    contained = (r1.start <= r2.start and r1.stop >= r2.stop) or (r2.start <= r1.start and r2.stop >= r1.stop)
    overlap = (r1.start <= r2.stop and r2.start <= r1.stop) or (r2.start <= r1.stop and r1.start <= r2.stop)
    
    return contained, overlap

if __name__ == "__main__":
    main(sys.argv[1])
