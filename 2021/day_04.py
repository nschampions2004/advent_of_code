from pathlib import Path

input_file = Path('data/day_04')

def called_out_numbers(path):
    with open(path) as f:
        input_data = f.readline()
    return input_data


if __name__ == "__main__":
    # print(called_out_numbers(input_file.joinpath('input.txt')))



    # for i in range()
    with open(input_file.joinpath('input.txt')) as f:
        input_data = f.read().splitlines()[2:]

    input_data = [row for row in input_data if row != '']

    number_of_boards = len(input_data) / 5
    boards = []
    for i in range(int(number_of_boards)):
        series = []
        for j, row in enumerate(input_data):
            if int(j) / number_of_boards == i:
                series.append(row)
        boards.append(series)

    print(input_data)
    print(number_of_boards)
    print(boards)

