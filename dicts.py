#
# dicts like hashmap, key value pairs
slang = {'cheerio':'goodbye', 'knackered':'tired', 'yonks':'ages'}
print(slang)

print(slang['cheerio'])

#to initialize
bdays = {'Bill' : 1967, 'Joyce' : 1966, 'V' : 1966, 'Owen' : 2007}
print(bdays)
print('Joyce', bdays['Joyce'])

#to init empty
test_dict = {}
test_dict['Rangers'] = 'New York'
test_dict['Bruins'] = 'Boston'
test_dict['Senators'] = 'Ottawa'
print(test_dict)

#to update just change value
test_dict['Rangers'] = 'NY'
print(test_dict)

#to remove use del
del test_dict['Senators']
print(test_dict)

#best way to lookup value is with get() and then check if None
results = test_dict.get('Rangers1')
print(results) #will be None

#check for null
if results == None:
    print("no key was found!!")

#or can do it this way
if results:
    print('Results=', results)
else:
    print('No results found')

# dict that contains a list    
families = {"Leonard Filler" : ["Bill", "Joyce"],
            "William Filler" : ["Owen", "Eliza", "Mia"],
            "Jim O'Brien" : ["Brendan", "Justin", "Rowan", "Evan"]}

print(families.get("Leonard Filler")[1])

# iterate over dict
for key in families:
    print("Family key", key, "Family value", families[key])

# use dict.items() in the for loop
# this gives you a key/value pair
menu_prices = {'Knackered Spam': 0.50, 'Pip pip Spam': 1.50, 'Squidgy Spam' : 2.50}
for name, price in menu_prices.items():
    print(name, ": $", format(price, '.2f'), sep='')

# keys are dict.keys() 
print(menu_prices.keys())
# values are dict.values()
print(menu_prices.values())

#this seems the easiest to me
for key in menu_prices.keys():
    print("key=", key, " value=", format(menu_prices.get(key), ".2f"))


