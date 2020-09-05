tot = 0

n = int(input('Digite um número: '))
for i in range(1, n+1):
    if n % i == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(i), end=' ')
print('\n O número {} foi divisível {} vezes'.format(n, tot))
if tot == 2:
    print('\n E por isso ele é PRIMO!')
else:
    print(' E por isso ele NÂO È PRIMO!')