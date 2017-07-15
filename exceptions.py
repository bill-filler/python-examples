#generic catch, no full error
try:
    file = open('xxyz.txt', 'r')
    print(file.read())
except:
    print("File doesn't exist")

#generic catch, put print specific exception
try:
    file = open('xxyz.txt', 'r')
    print(file.read())
except Exception as err:
    print("File doesn't exist", err)

#specific exceptions to catch
#http://go.codeschool.com/python-exceptions
price = input("Enter the price: ")
try:
    price = float(price)
    print('Price =', price)
except ValueError as err:
    print('Not a number!', err)
