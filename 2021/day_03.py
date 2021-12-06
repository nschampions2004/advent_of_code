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


if __name__ == "__main__":
    data_path = Path('data/day_03')
    with open(data_path.joinpath('input.txt')) as f:
        binary_file = f.read().splitlines()

    submarine_report = BinaryDiagnostic(binary_file)
    # solution 1
    rates = submarine_report.rates()
    print(rates[0] * rates[1])




