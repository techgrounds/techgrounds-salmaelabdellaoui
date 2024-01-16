# Exercise 1
'''
The output should be:
hello Casper
hello Floris
hello Esther
'''
foo = 'hello'
ls = ['Casper', 'Floris', 'Esther']
for name in ls:
	print(foo, name)
	
# Exercise 2
'''
The output should be:
100
'''
foo = 20
bar = '80'
print(foo + int(bar))

# Exercise 3
'''
The output should be:
30
'''
foo = 20
for i in range(10):
	foo += 1

print(foo)

# Exercise 4 
'''
The output should be:
there are 0 kids on the street
there are 1 kids on the street
there are 2 kids on the street
there are 3 kids on the street
there are 4 kids on the street
'''
foo = 0
while foo < 5:
	print('there are', foo, 'kids on the street')
	foo += 1

# Exercise 5
'''
The output should be:
Star Wars
'''
ls = ['Lord of the rings', 'Star Trek', 'Iron Man', 'Star Wars']
print(ls[3]) 