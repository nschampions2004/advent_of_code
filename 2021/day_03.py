import pandas as pd
import numpy as np
from pathlib import Path

class BinaryDiagnostic:
    def __init__(self, binary_file):
        self.binary_file = binary_file
        return

    def rates(self):
        """ calculates the gamma and epsilon rates for a given binary list"""

        gamma = []
        eps = []
        binary_width = len(self.binary_file[0])

        for i in range(binary_width):
            first_bit = np.array([int(row[i]) for row in self.binary_file])
            length = first_bit.shape[0]
            ones = np.count_nonzero(first_bit)
            zeros = length - ones

            if ones > zeros:
                gamma.append('1')
                eps.append('0')
            else:
                gamma.append('0')
                eps.append('1')

        gamma_rate = int(''.join(gamma), 2)
        epsilon_rate = int(''.join(eps), 2)

        return gamma_rate, epsilon_rate

    def oxygen_rating(self):
        """ calculate the oxygen rating """

        """ looping through the bits
            1. figure out whether ones or zeroes appear the most
            2. filter to only those entries with the most in the index
            3. do it again for the second entry... so forth and so on
        """

        binary_width = len(self.binary_file[00])

        keep = np.array([row for row in self.binary_file])
        for i in range(binary_width): # switch to length of binary file
            # if len(keep) > 1:
            length = keep.shape[0]
            ones = np.count_nonzero(keep)
            zeros = length - ones

            if ones > zeros:
                print("ones more frequent")
                keep_grp = '1'
            else:
                print("zeroes more frequent")
                keep_grp = '0'

            # import pdb; pdb.set_trace()

            keep = np.array([row for row in keep if str(row)[i] == keep_grp])
            print(keep[0:5])
        assert(len(keep) == 1)

        return keep[0], keep

    def life_support_rating(self):

        return #o2_gen * co2_scrubber


if __name__ == "__main__":
    data_path = Path('data/day_03')
    with open(data_path.joinpath('input.txt')) as f:
        binary_file = f.read().splitlines()

    submarine_report = BinaryDiagnostic(binary_file)
    # solution 1
    rates = submarine_report.rates()
    # print(rates[0] * rates[1])
    #
    # # solution 2
    # print(submarine_report.binary_file[0:5])
    # print(submarine_report.oxygen_rating())




    test = ['011101101110', '010110001101', '100111000110', '011110101000', '101101000100']

    """ """
    ones = 0
    zeros = 0
    for place in range(len(test[0])):
        for i in test:
            # import pdb; pdb.set_trace()
            if i[place] == '0':
                zeros += 1
            else:
                ones += 1
    print(f"{zeros} zeros, {ones} ones")

