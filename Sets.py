# Unfolding a list of lists for sets
# Example list of lists
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Unfold the list of lists and add elements to a set
unfolding_set = {element for sublist in list_of_lists for element in sublist}

print(unfolding_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}
