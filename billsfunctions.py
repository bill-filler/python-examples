import random

def gen_random(start_val, end_val):
    return random.randint(start_val, end_val)

#print contents of file using the read() function
def print_file_contents(filename):
    the_file = open(filename, 'r')
    contents = the_file.read()
    print(contents)
    the_file.close()
