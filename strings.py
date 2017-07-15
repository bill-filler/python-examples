line = 'Billy Filler - 04/13/67'
# this will create name value pair ['Billy Filler', '04/13/67']
print(line.split(' - '))

(name, birthday) = line.split(' - ');
print(name, birthday)

#strip will get rid of leading/trailing whitespace/newlines
line = 'Billy Filler\n'
print(line)
print(line.strip())
