spisok = [1, 1]
def stupenki(n):
    if n < len(spisok):
        return spisok[n]
    p = stupenki(n - 1) + stupenki(n - 2)
    spisok.append(p)
    return p

try:
    a = int(input('Введите число ступенек: '))
    print(stupenki(a))
except ValueError:
    print('Вводите только числа!')