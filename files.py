
# write the key/values from passed in dict to file
def write_dict(filename, mode, the_dict):
    the_file = open(filename, mode)
    for key, value in the_dict.items():
        the_string = key + ' - ' + value + '\n'
        the_file.write(the_string)
    
    the_file.close()


def write_file(filename, mode, lines):
    the_file = open(filename, mode)
    for line in lines:
        the_file.write(line + '\n')
    the_file.close()

#reads file line by line
def read_file(filename):
    the_file = open(filename, 'r');
    #note can also use the_file.readline() to read next line
    #but not sure how to iterate over them
    for line in the_file:
        print(line)
    the_file.close()

#print contents of file using the read() function
def print_file_contents(filename):
    the_file = open(filename, 'r')
    contents = the_file.read()
    print(contents)
    the_file.close()

#return the contents of the file as a list
def get_file_as_list(filename):
    the_file = open(filename, 'r');
    the_list = []
    for line in the_file:
        the_list.append(line.strip())
    the_file.close()
    return the_list
    
def main():
    #write_file('spam_orders.txt', 'w', ['Sales Log', 'The Spam Van', 'Willy Brown'])

    #performances = {'Ventriloquism': '9:00am', 'Snake Charmer': '12:00pm', 'Amazing Acrobatics':  '2:00pm', 'Enchanted Elephants': '2:00pm'}
    #write_dict('performances.txt', 'w', performances)

    #read_file('input.txt')
    #print_file_contents('input.txt')
    items = get_file_as_list('input.txt')
    print(items)

main()
