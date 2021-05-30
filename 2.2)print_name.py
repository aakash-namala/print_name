#program to print name
name=input('Enter the name: ')
n=int(input('how many times you want to print your name: '))

print('\nPrinting the name side by side:')
for i in range(n):
    print(name,end='  ')

    
print('\n\nPrinting the name line by line:')
for i in range(n):
    print(name)
