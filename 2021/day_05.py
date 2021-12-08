from pathlib import Path


def convert_to_tuple(element):
    start_point = (element[0].split(','))
    start_point_x = int(start_point[0])
    start_point_y = int(start_point[1])

    end_point = (element[1].split(','))
    end_point_x = int(end_point[0])
    end_point_y = int(end_point[1])

    start_point = (start_point_x, start_point_y)
    end_point = (end_point_x, end_point_y)

    return (start_point, end_point)


def diagonal_eliminator(tuple):
    if (tuple[0][0] == tuple[1][0]) or (tuple[0][1] == tuple[1][1]):
        return True
    else:
        return False

def everything_in_between(tuple):

    first_point = tuple[0]
    second_point = tuple[1]

    vertical = True if first_point[0] == second_point[0] else False

    if vertical:
        larger = max(first_point[1], second_point[1])
        smaller = min(first_point[1], second_point[1])
        diff = larger - smaller

        in_between = []
        for i in range(diff + 1):
            in_between.append((first_point[0], smaller + i))

    else:
        larger = max(first_point[0], second_point[0])
        smaller = min(first_point[0], second_point[0])
        diff = larger - smaller

        in_between = []
        for i in range(diff + 1):
            in_between.append((smaller + i, first_point[1]))

    return in_between

if __name__ == "__main__":

    # solution 1
    input_data = Path('data/day_05')
    with open(input_data.joinpath('input.txt')) as f:
        lines = f.read().splitlines()

    divided = [el.split(' -> ') for el in lines]
    tuples = [convert_to_tuple(element) for element in divided]
    non_diag = [tuple for tuple in tuples if diagonal_eliminator(tuple)]

    max_value = max([x[0][i] for x in non_diag for i in range(2)])

    diagram = np.zeros(shape=(max_value, max_value))

    point_holder = []
    for tup in non_diag:
        point_holder.append(everything_in_between(tup))

    for collection in point_holder:
        for point in collection:
            diagram[point[0] - 1, point[1] - 1] += 1
