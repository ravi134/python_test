str = ''
k = int(input('Enter a number of lines:'))

for i in range(1,k+1):  
    str = ' ' * (k - i) + '*' * i + '' + '*' * (i)
    print(str)
    
for i in range(k,0,-1):
    str = '*' * (i) + ' ' * (k - i) + '' + ' ' * (k - i) + '*' * i
    print(str)

print(' ')
print(' ')

for i in range(k,0,-1):
    str = '*' * (i) + ' ' * (k - i) + '' + ' ' * (k - i) + '*' * i
    print(str)

for i in range(k,0):
    str = '*' * (i) + ' ' * (k - i) + '' + ' ' * (k - i) + '*' * i
    print(str)
