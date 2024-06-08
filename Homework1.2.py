while True:
    a = input('Введите целое число от 1 до 999\n')
    list_of_numbers = [
    ['один','два','три','четыре','пять','шесть','семь','восемь','девять'],
    ['десять','одиннадцать','двенадцать','тринадцать','четырнадцать','пятнадцать','шестнадцать','семнадцать','восемнадцать','девятнадцать'],
    ['двадцать','тридцать','сорок','пятьдесят','шестьдесят','семьдесят','восемьдесят','девяносто'],
    ['сто','двести','триста','четыреста','пятьсот','шестьсот','семьсот','восемьсот','девятьсот']]
    while True:
        if not a.isdigit():
            a = input('Falsch. Введите целое число от 1 до 999.\n')
        elif not ( 1 <= int(a) <= 999):
            a = input('Falsch. Введите целое число от 1 до 999.\n')
        else:
            break
    if len(a) == 1:
        res = list_of_numbers[0][int(a)-1]
        print(res)
    elif len(a) == 2:
        if a[0] == '1':
            res = list_of_numbers[1][int(a[1])]
            print(res)
        elif a[0] != '1':
            if a[1] != '0':
                res = list_of_numbers[2][int(a[0])-2]  + ' ' +  list_of_numbers[0][int(a[1])-1]
                print(res)
            else:
                res = list_of_numbers[2][int(a[0])-2]
                print(res)
    else:
        if a[1] == '0' and a[2] == '0':
            res = list_of_numbers[3][int(a[0])-1]
            print(res)
        elif a[1] == '0' and a[2] != '0':
            res = list_of_numbers[3][int(a[0])-1] + ' ' + list_of_numbers[0][int(a[2])-1]
            print(res)
        elif a[1] != '0' and a[2] == '0':
            res = list_of_numbers[3][int(a[0])-1] + ' ' + list_of_numbers[2][int(a[1])-2]
            print(res)
        elif a[1] != '0' and a[2] != '0':
            if a[1] == '1':
                res = list_of_numbers[3][int(a[0])-1] + ' ' + list_of_numbers[1][int(a[2])]
                print(res)
            else:
                res = list_of_numbers[3][int(a[0]) - 1] + ' ' + list_of_numbers[2][int(a[1])-2] + ' ' + list_of_numbers[0][int(a[2])-1]
                print(res)


