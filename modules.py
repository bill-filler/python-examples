# only thing that is needed to make your own module is just put functions
# in a file names <module_name>.py
import billsfunctions

def test_modules():
    # call a function from billsfunctions module (defined in billsfunctions.py)
    rando = billsfunctions.gen_random(1,1000)
    print(rando)

    billsfunctions.print_file_contents('input.txt')

def main():
    test_modules()

main()
