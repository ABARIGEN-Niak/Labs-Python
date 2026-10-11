Ax = int(input('Введите кординату точки А на оси x '))
Ay = int(input('Введите кординату точки А на оси y '))
Cx = int(input('Введите кординату точки C на оси x '))
Cy = int(input('Введите кординату точки C на оси y '))
if(Ax > Cx and Ay > Cy):
    Ax, Cx = Cx, Ax
    Ay, Cy = Cy, Ay
elif(Ax > Cx):
    Ax, Cx = Cx, Ax
elif(Ay > Cy):
    Ay, Cy = Cy, Ay
side_vert = Cx - Ax
side_gor = Cy - Ay
if(side_vert != side_gor):
    print('Это не квадрат!')
else:
    per = side_vert * 4
    plosh = side_vert * side_vert
    print('Периметр квадрата равен ', per,' а площадь равна ', plosh)