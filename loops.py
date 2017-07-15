import random

prices = [2.50, 3.50, 3.25]
total = 0

for price in prices:
    total = total + price

#print every character of the word on a new line
word = 'Welcome!'
for char in word:
    print(char)

average_price = total / len(prices)
print("Total=", total)
print("Average Price=", average_price)

#random int between 0-10
randNum = random.randint(0,10)
print(randNum)

#print 10 random numbers from 1-1000
for i in range(10):
    print("i=", i)
    print(random.randint(0,10))

#try range(start, stop, step) values
#i will start at 2007 and increment by 2 while < 2018
for i in range(2007, 2018, 2):
    print(i)

r2 = random.choice([1,2,3,4,5])
print(r2)

# generate a list of numbers from 0-19
my_list = range(20)
for i in my_list:
    print(i)


#while loops
i = 0
while i < 5:
    print(i)
    i = i + 1

# use continue and break as well
i = 0
while (True):
    if i < 5:
        print(i)
        i = i + 1
        continue
    else:
        break;

# choose a random number game
num = random.randint(1,10)

guess = int(input('Guess a number between 1 and 10:\n'))
times = 1
while guess != num:
    guess = int(input('Guess again:\n'))
    times = times + 1
    if times == 3:
        break

if guess == num:
    print('You win!')
else:
    print('You lose! The number was ', num)

    
