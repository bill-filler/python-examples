#
# lists
#

#empty list
foo = []
bar = ["a", "b", "c"]

#append
bar.append("d")
print(bar)
bar.remove("d")
print(bar)

#range to get some items in list
print(bar[:1])

#remove by value
bar.remove("c")
print(bar)

#remove by index
del bar[0]
print(bar)

# list of lists
menus = [["Bill", "Joyce"],
         ["Owen", "Eliza", "Mia"],
         ["Brendan", "Justin", "Rowan", "Evan"]]

print(menus[0])
