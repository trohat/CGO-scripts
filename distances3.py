# function for calculating distances between positions in a grid, e.g. on a board
def calculate_distances():
    first_dist = int(input("Enter first distance: "))
    last_dist = int(input("Enter last distance: "))
    real_dim = int(input("Enter real dimension: "))
    options_dim = int(input("Enter options dimension: "))
    points = int(input("Enter number of points: "))
    divider = real_dim / options_dim
    print("Divider", divider)
    first_dist = first_dist / divider
    last_dist = last_dist / divider
    print("First distance", first_dist)
    print("Last distance", last_dist )
    iters = points - 1
    diff = (last_dist - first_dist) / iters
    print("Diff", diff)

calculate_distances()