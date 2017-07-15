#calculate the average value of the list passed in
def average(numbers):
    total = 0
    for number in numbers:
        total = total + number

    avg = total/len(numbers)
    return avg

def main():
    the_avg = average([5, 10, 15])
    print(the_avg)

main()

