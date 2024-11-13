n = int(input('Введите целое число от 3 до 20: '))
if n <= 2:
    print('Число вне диапазона')
elif n >= 21:
    print('Число вне диапазона') #не понимаю почему в данном случае не работает условие "and"
else:                        # например пишу if c <= 2 and c >= 21, то при вводе чисел меньше 3х и больше 20 программа все равно работает, подбирает пары чисел
    for n in range(3,21):
        string = ''
        for a in range(1,n):
            for b in range(a+1,n):
                if n%(a+b) == 0:
                    string = string + str (a) + str (b)
        print(n, ' - ', string)

