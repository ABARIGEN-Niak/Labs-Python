ladia_x = int(input('Кординаты белого ладьи на оси x(от 1 до 8) '))
ladia_y = int(input('Кординаты белого ладьи на оси y(от 1 до 8) '))

ferz_x = int(input('Кординаты черного ферзя на оси x(от 1 до 8) '))
ferz_y = int(input('Кординаты черного ферзя на оси y(от 1 до 8) '))

step_x = int(input('Куда пойти ладье по оси x(от 1 до 8) '))
step_y = int(input('Куда пойти ладье по оси y(от 1 до 8) '))
if(step_x == ladia_x or step_y == ladia_y):
    print('NO CORRECT')
elif(step_x == ferz_x or step_y == ferz_y or step_x - step_y == ferz_x - ferz_y or step_x + step_y == ferz_x + ferz_y):
    print('NO')
else:
    print('YES')
#Расчет белого ладьи и черного ферзя

crown_x = int(input('Кординаты белого короля на оси x(от 1 до 8) '))
crown_y = int(input('Кординаты белого короля на оси y(от 1 до 8) '))

horse_x = int(input('Кординаты черного коня на оси x(от 1 до 8) '))
horse_y = int(input('Кординаты черного коня на оси y(от 1 до 8) '))

step2_x = int(input('Куда пойти королю по оси x(от 1 до 8) '))
step2_y = int(input('Куда пойти королю по оси y(от 1 до 8) '))

dx = abs(step2_x - horse_x)
dy = abs(step2_y - horse_y)
if(step2_x > crown_x + 1 or step2_x < crown_x - 1 or step2_y > crown_y + 1 or step2_y < crown_y - 1):
    print('NO CORRECT')
elif(step2_x == crown_x and step2_y == crown_y):
    print('Ну стой на месте значит')
elif(dx == 1 and dy == 2) or (dx == 2 and dy == 1):
    print('NO')
else:
    print('YES')