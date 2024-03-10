# Bundle exercise
# List of overstock items with their names and prices
overstock_items = [['shirt_103985', 15.99],
                    ['pants_906841', 19.99],
                    ['pants_765321', 15.99],
                    ['shoes_948059', 29.99],
                    ['shoes_356864', 9.99],
                    ['shirt_865327', 10.99],
                    ['shorts_086853', 9.99],
                    ['pants_267953', 21.99],
                    ['dress_976264', 32.99],
                    ['shoes_135786', 17.99],
                    ['skirt_196543', 12.99],
                    ['jacket_976535', 26.99],
                    ['pants_086367', 30.99],
                    ['dress_357896', 29.99],
                    ['shoes_157895', 14.99]]

from collections import deque, namedtuple

# Create a deque (double-ended queue) to store split prices
split_prices = deque()

# Split the prices into two groups: prices over $20 and prices $20 or below
for item in overstock_items:
    if item[1] > 20:
        split_prices.appendleft(item)  # Add high-priced items to the left
    else:
        split_prices.append(item)  # Add low-priced items to the right

# Print the split prices
print(split_prices)

# Define a named tuple 'ClothesBundle' to represent a bundle of clothes with bundle items and bundle price
ClothesBundle = namedtuple('ClothesBundle', ['bundle_items', 'bundle_price'])

# Create a list to store bundles
bundles = []

# Create bundles with 5 items each until there are fewer than 5 items left in split_prices
while len(split_prices) > 4:
    # Pop and append items to form a bundle of 5 items
    bundle_list = [split_prices.pop(), split_prices.pop(), split_prices.pop(), split_prices.popleft(), split_prices.popleft()]
    
    # Calculate the total price of the bundle
    total_price = 0
    for x in bundle_list:
        total_price += x[1]
    
    # Create a ClothesBundle instance and append it to the list of bundles
    bundles.append(ClothesBundle(bundle_list, total_price))

# Filter promoted bundles with a total price greater than $100
promoted_bundles = [x for x in bundles if x[1] > 100]

# Print the promoted bundles
print(promoted_bundles)
