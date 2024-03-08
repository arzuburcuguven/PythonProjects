guests = {}

def read_guestlist(file_name):
  text_file = open(file_name,'r')

  while True:
    line_data = text_file.readline().strip().split(",")
    new_guest = yield line_data
    #Create the if-else syntax that enables the .send function append the guest list
    if new_guest != None:
      line_data = new_guest.split(",")
    else:
      if len(line_data) < 2:
    # If no more lines, close file
        text_file.close()
        break
    name = line_data[0]
    age = int(line_data[1])
    guests[name] = age


# Retrieve the generator object
guestlist_generator = read_guestlist('guest_list.txt')

# Iterate through the generator object using a for loop and print the first 10 guests
for _ in range(10):
    print(next(guestlist_generator))

#Add Jane to the list
print(guestlist_generator.send("Jane, 35"))

#Complete reading the guest list file
for _ in range(4):
  print(next(guestlist_generator))

#print guest dictionary
print(guests)

#Define mock table generators that yield tuples of food item, table number and seat number.
def table_gen_1():
  food_list = ["Chicken", "Fish", "Beef", "Chicken", "Fish"]
  for i in range(1,6):
    yield (food_list[i-1], "Table 1", "Seat {}".format(i))
def table_gen_2():
  food_list = ["Chicken", "Fish", "Beef", "Chicken", "Fish"]
  for i in range(1,6):
    yield (food_list[i-1], "Table 2", "Seat {}".format(i))
def table_gen_3():
  food_list = ["Chicken", "Fish", "Beef", "Chicken", "Fish"]
  for i in range(1,6):
    yield (food_list[i-1], "Table 3", "Seat {}".format(i))

#Connect the table generators
def connected_gen_func():
  yield from table_gen_1()
  yield from table_gen_2()
  yield from table_gen_3()

#Assign guests to tables
def assign_table(a_list, gen):
    my_gen = gen()  # Create a generator object
    for i in a_list:
        try:
            yield (i, next(my_gen))  # Yield a tuple with element from a_list and next value from my_gen
        except StopIteration:
            print('Tables are full or all guests are seated')
            break


assigner = assign_table(guests, connected_gen_func)
for x in range(16):
  print(next(assigner))

