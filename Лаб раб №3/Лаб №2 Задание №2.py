circle = float(input("Введите площадь круга "))
square = float(input("Введите площадь квадрата "))
rad_circle = (circle / 3.14) ** 0.5
side_square = square ** 0.5
diag_square = side_square * (2 ** 0.5)
if(diag_square <= 2 * rad_circle):
    print('Этот квадрат поместиться в круг')
else:
    print('Этот квадрат НЕ поместиться в круг')
