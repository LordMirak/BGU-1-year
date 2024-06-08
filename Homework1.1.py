a = input('Введите целое положительное число строк.\nN = ')
while True:
    if not a.isdigit():
        a = input('Falsch. Введите целое положительно число строк.\nN = ')
    elif int(a) < 0:
        a = input('Falsch. Введите целое положительно число строк.\nN = ')
    else:
        a = int(a)
        break
b = 1
c = a - 1
for i in range(a):
    print(c*' '+('*'*b))
    b = b + 2
    c = c - 1



