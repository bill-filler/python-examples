num_knights =  int(input('Enter number of knights:\n'))
fallback_string = 'xxx Oh Crapyoustink'
#print(num_knights)

if num_knights <= 3:
    print('less than or equal to 3')
elif num_knights > 3 and num_knights <= 6:
    print('between 4 and 6')
elif num_knights > 6 and num_knights <= 10:
    print('between 7 and 10')
else:
    print('greater than 10')
    if fallback_string.lower().find('oh crap') != -1:
        print('first fallback', fallback_string)
    else:
        print('second fallback', fallback_string)
