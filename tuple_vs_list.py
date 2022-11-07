# tuple vs list

colors_list = ['red', 'pink', 'blue', 'yellow']
colors_tuple = ('red', 'pink', 'blue', 'yellow')

# replacing yellow with gray - list

colors_list[3] = 'gray'
print(colors_list)

# replacing yellow with gray - tuple

colors_tuple[3] = 'gray'
print(colors_tuple) # will not work, gives an error: 'tuple' object does not support item assignment



