# pylint: disable=invalid-name
"""
Code uses chinese remainder thoerum to calculate the christmas tree
Copied from a reddit user: i_have_no_biscuits
"""

from re import findall
from statistics import variance as var

# Read the data from the file
with open("input.txt", "r", encoding="utf8") as file:
    data = file.read()

# Define the width and height of the space
W, H = 101, 103

# Parse the data to extract values for p (sx, sy) and v (vx, vy)
robots = [
    [int(n) for n in findall(r"(-?\d+)", item)]  # Extract integers from each line
    for item in data.splitlines()  # Split the data by lines
]

# Check that robots have 4 values (sx, sy, vx, vy)
for robot in robots:
    if len(robot) != 4:
        print(f"Invalid robot data: {robot}")


# Function to simulate the movement of robots over time
def simulate(t):
    """simulating"""
    return [((sx + t * vx) % W, (sy + t * vy) % H) for (sx, sy, vx, vy) in robots]


bx = min(range(W), key=lambda t: var((s + t * v) % W for (s, _, v, _) in robots))
by = min(range(H), key=lambda t: var((s + t * v) % H for (_, s, _, v) in robots))

print("Part 2:", bx + ((pow(W, -1, H) * (by - bx)) % H) * W)
