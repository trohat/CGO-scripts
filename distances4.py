# function for calculating distances between positions in a grid, e.g. on a board
def calculate_distances():
    dist = int(input("Enter distance: "))
    real_dim = int(input("Enter real dimension: "))
    options_dim = int(input("Enter options dimension: "))
    divider = real_dim / options_dim
    print("Divider", divider)
    dist = dist / divider
    print("Distance", dist )

calculate_distances()