try:
    with open('input.txt', 'r') as file:
        with open('output.txt', 'w') as lacock:
            d = file.readlines()
            a = input('Введите символы для удаления:\n') + ';' + '\n'
            for i in d:
                result = i.rstrip(a)
                print(result[::-1], file=lacock)

except FileNotFoundError:
    print('This file does not exist. Please come back later')