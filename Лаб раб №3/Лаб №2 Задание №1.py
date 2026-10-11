a = int(input('Введите первое число '))
b = int(input('Введите второе число '))
c = int(input('Введите третье число '))
if(a != b != c):
    if(a > b) and (a > c):
        res = b + c
        print(res)
    if(b > a) and (b > c):
        res = a + c
        print(res)
    if(c > a) and (c > b):
        res = a + b
        print(res)
else:
    a, b, c = 0
    print(a, b, c)