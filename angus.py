"""
This file runs a simulation for the situation posed in 
https://www.theguardian.com/science/2024/sep/30/can-you-solve-it-the-box-problem-that-baffled-the-boffins.
"""

import random

# Store useful constants
ROWS = 3
COLS = 5
SPOTS = 15
# 2D array of boxes
# Each box starts as "False". In the simulation, a box will be marked "True" if it stores a prize.
boxes = [[False]*5 for i in range(3)]

# The main functionality of the file: runs the simulation with a number of different seeds
def main():
    n = 1000000
    sim(n)
    sim(n, seed="Patrick")
    sim(n, seed="Guardian")
    sim(n, seed="Comment")
    sim(n, seed="Random")

# Simulation description
def sim(n : int, seed="Angus"):
    # Seed the pseudorandom generator
    random.seed(seed) 
    # This table will store how many times each person has won
    winners = {"Andrew" : 0, "Barbara" : 0, "Draw" : 0} 
    # Run the following code n times
    for _ in range(n):
        # Randomly generate two prize positions
        p1 = random.randint(0, SPOTS - 1)
        p2 = random.randint(0, SPOTS - 1)
        # Make sure prize 2 is in a different box to prize 1
        while (p2 == p1):
            p2 = random.randint(1, SPOTS - 1)
        # Mark the prize boxes
        boxes[p1 // COLS][p1 % COLS] = True
        boxes[p2 // COLS][p2 % COLS] = True
        andrew = [0,0]
        barbara = [0,0]
        # While neither of them have won, make each of them check the next box
        while not (boxes[andrew[0]][andrew[1]] or boxes[barbara[0]][barbara[1]]):
            a_move(andrew)
            b_move(barbara)
        # Update winners based on who reached the prize
        if boxes[andrew[0]][andrew[1]] and boxes[barbara[0]][barbara[1]]:
            winners["Draw"] += 1
        elif boxes[andrew[0]][andrew[1]]:
            winners["Andrew"] += 1
        elif boxes[barbara[0]][barbara[1]]:
            winners["Barbara"] += 1
        # If there isn't a winner, the program has gone wrong - exit out!
        else:
            raise Exception("Nobody won somehow?!")
        # Take the prizes out of the box
        boxes[p1 // COLS][p1 % COLS] = False
        boxes[p2 // COLS][p2 % COLS] = False  
    # Once we've completed the loop, print the results!
    print(f"Seed: {seed}, iterations: {n}, results: {winners}")
    return winners

# Andrew moves along the rows
def a_move(a):
    a[1] += 1
    if a[1] >= COLS: 
        a[0] += 1
        a[1] = 0

# Andrew moves along the columns
def b_move(b):
    b[0] += 1
    if b[0] >= ROWS: 
        b[0] = 0
        b[1] += 1

# Run the main function when this file is started
if __name__ == "__main__":
    main()