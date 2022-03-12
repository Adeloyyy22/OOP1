while True:
    a = float (input("Bведите первое число"))
    b = (input('Введите операцию(+ - * /)'))
    c = float(input('Ввидите второе число:'))

    if b=='+':
        answer = a+c
        print(answer)

    elif b =='-':
        answer = a-c
        print(answer)
    elif b=="*":
        answer = a*c
        print(answer)
    elif b=="/" and c==0:
        print('нельзя делить на 0!!!')
    elif b=='/':
        answer = a/c
        print(answer)
    else:
        print("не опознная операция!!")



