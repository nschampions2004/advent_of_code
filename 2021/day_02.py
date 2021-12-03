import pandas as pd
from pathlib import Path
import numpy as np

# save https://adventofcode.com/2021/day/1/input as .txt file
# solution 2
class SubmarineNavigation:

    def __init__(self):
        self.nav_path = None
        self.location = (0,0)
        self.aim = 0

    def set_nav_path(self, input_file):

        with open(input_file) as f:
            self.nav_path = f.readlines()
        return print("set nav path")

    def row_split(self, row):
        dir_dist = row.split()

        return dir_dist[0], dir_dist[1]


    def step(self, row):
        dir, dist = self.row_split(row)

        initial_loc = self.location

        if dir == "forward":
            self.location = (self.location[0] + int(dist), self.location[1])

        elif dir == "down":
            self.location = (self.location[0], self.location[1] + int(dist))
        elif dir == "up":
            self.location = (self.location[0], self.location[1] - int(dist))
        else:
            print("ERROR")

        return print(f"sub moved from {initial_loc} to {self.location}")

    def step_with_aim(self, row):
        dir, dist = self.row_split(row)

        initial_loc = self.location
        initial_aim = self.aim

        if dir == "forward":
            hor = self.location[0] + int(dist)
            depth = self.aim * int(dist)
            self.location = (hor, self.location[1] + depth)
        elif dir == "down":
            self.aim = self.aim + int(dist)
        elif dir == "up":
            self.aim = self.aim - int(dist)
        else:
            print("ERROR")

        return print(f"sub moved {dir} from {initial_loc} to {self.location} with aim {self.aim}")


if __name__ == '__main__':
    # data file
    data = Path('data/day_02')

    sub_path = SubmarineNavigation()

    sub_path.set_nav_path(data.joinpath('input.txt'))

    for i, row in enumerate(sub_path.nav_path):
        sub_path.step(row)

    # solution 1
    print(sub_path.location[0] * sub_path.location[1])

    # solution 2
    sub_path.location = (0,0)
    for i, row in enumerate(sub_path.nav_path):
        sub_path.step_with_aim(row)
    print(sub_path.location[0] * sub_path.location[1])
