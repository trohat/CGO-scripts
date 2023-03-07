# function for calculating distances between positions in a grid, e.g. on a board
def calculate_distances():
    options_dim = int(input("Enter options dimension: "))
    real_dim = int(input("Enter real dimension: "))
    dist = int(input("Enter first distance: "))
    distances = [dist]
    while True:
        dist = int(input("Enter next distance, 0 for quit and calculate: "))
        if dist == 0:
            break
        distances.append(dist)
    divider = real_dim / options_dim
    print("Divider", divider)
    print("Distances", distances)
    real_distances = [d / divider for d in distances]
    print("Real distances", real_distances)

    print("First distance: ", real_distances[0])

    first_distances = real_distances[:-1]
    second_distances = real_distances[1:]

    diffs = []
    for i in range(len(first_distances)):
        diffs.append(second_distances[i] - first_distances[i])
    print("Diffs", diffs)
    avg_diff = sum(diffs) / len(diffs)
    print("Avg diff", avg_diff)

calculate_distances()