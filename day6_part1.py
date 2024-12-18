import numpy as np
from typing import Tuple
from collections import defaultdict

def parseTxtToArr(path: str):
    data = open(path).read().splitlines()
    data = [list(line) for line in data]
    return np.array(data)

def findStartingPos(arr) -> Tuple[int, int]:
    pos = [idx for idx, val in np.ndenumerate(arr) if val == "^"]
    return pos[0]

def countUniquePos(arr) -> int:
    
    starting_pos = findStartingPos(arr)
    pos_dict = defaultdict(int)
    
    # Direction vectors: up, right, down, left
    turn_dict = {
        0: (0, 1),   # Moving right
        1: (1, 0),   # Moving down
        2: (0, -1),  # Moving left
        3: (-1, 0)   # Moving up
    }
    
    nrow, ncol = arr.shape
    i, j = starting_pos
    turn_dict_idx = 0

    while (0 <= i < nrow) and (0 <= j < ncol):
        # Mark the current position as visited
        pos_dict[(i, j)] += 1
        
        # Calculate the next step
        next_step = turn_dict[turn_dict_idx]
        next_i, next_j = i + next_step[0], j + next_step[1]
        
        # Check for boundaries
        if 0 <= next_i < nrow and 0 <= next_j < ncol:
            if arr[next_i, next_j] != "#":
                # Move to the next position
                i, j = next_i, next_j
            else:
                # Encounter a blocker, turn 90 degrees to the right
                turn_dict_idx = (turn_dict_idx + 1) % 4
        else:
            # Out of bounds, break the loop
            break

    return len(pos_dict)

if __name__ == "__main__":
    input_path = "data/input_day6_part1.txt"
    arr = parseTxtToArr(input_path)
    unique_pos = countUniquePos(arr)
    print(unique_pos)