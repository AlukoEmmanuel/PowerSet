def printPowerSet(my_set, set_size):
    power_set_size = 2 ** set_size
    for outer in range(power_set_size):
        for inner in range(set_size):
            # Check if jth bit in the outer is set. If set, print set[j]
            if outer & (1 << inner):
                print(my_set[inner], end=" ")
        print()  # Print new line after each subset

# Example usage
my_set = ['a', 'b', 'c']
printPowerSet(my_set, len(my_set))
