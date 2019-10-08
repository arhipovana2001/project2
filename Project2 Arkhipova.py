import math
# Данная программа определяет простую
# геометрическую фигуру и вычисляет ее площадь.
# В планиметрии это площадь фигуры.
# В стереометрии это площадь полной поверхности.
print('Это планиметрическая фигура?')
answer1 = str(input())
if answer1 == 'да':
        print('У этой фигуры есть вершины?')
        answer2 = str(input())
        if answer2 == 'да':
                print('У фигуры 3 вершины?')
                answer3 = str(input())
                if answer3 == 'нет':
                    print('У фигуры все углы прямые?')
                    answer4 = str(input())
                    if answer4 == 'да':
                        print('У фигуры все стороны равны?')
                        answer5 = str(input())
                        if answer5 == 'да':
                            print('Это квадрат, введите его сторону')
                            a = int(input())
                            s = a * a * 6
                            print('Площадь равна', s)
                        else:
                            print('Это прямоугольник, введите его стороны через пробел')
                            a, b = map(int, input().split())
                            s = a * b
                            print('Площадь равна', s)
                    else:
                        print('У фигуры все стороны равны?')
                        answer5 = str(input())
                        if answer5 == 'да':
                            print('Это ромб, введите его сторону и высоту через пробел')
                            a, h = map(int, input().split())
                            s = a * h
                            print('Площадь равна', s)
                        else:
                            print('Стороны попарно параллельны и равны?')
                            answer6 = str(input())
                            if answer6 == 'да':
                                print('Это параллелограмм, введите его сторону и высоту через пробел')
                                a, h = map(int, input().split())
                                s = a * h
                                print('Площадь равна', s)
                            else:
                                print('Это трапеция, введите ее верхнюю и нижнюю стороны и высоту через пробел')
                                a, b, h = map(int, input().split())
                                s = ((a + b) / 2) * h
                                print('Площадь равна', s)
                else:
                    print('Это треугольник, введите его сторону и высоту через пробел')
                    a, h = map(int, input().split())
                    s = 0.5 * a * h
                    print('Площадь равна', s)
        else:
            print('Это круг, введите его радиус')
            r = int(input())
            s = math.pi * r ** 2
            print('Площадь равна', s)
else:
    print('Это тело вращения?')
    answer2 = str(input())
    if answer2 == 'да':
        print('Тело можно создать, вращая окружность вокруг диаметра?')
        answer3 = str(input())
        if answer3 == 'да':
            print('Это шар, введите его радиус')
            r = int(input())
            s = 4 * math.pi * r * r
            print('Площадь равна', s)
        else:
            print('Тело можно создать, вращая прямоугольный треугольник вокруг своего катета?')
            answer3 = str(input())
            if answer3 == 'да':
                print('Это конус, введите его радиус и апофему через пробел')
                r, a = map(int, input().split())
                s = math.pi * r * (a + r)
                print('Площадь равна', s)
            else:
                print('Это цилиндр, введите его радиус и высоту через пробел')
                r, h = map(int, (input().split()))
                s = 2 * math.pi * r * (h + r)
                print('Площадь равна', s)
    else:
        print('У фигуры все ребра равны?')
        answer3 = str(input())
        if answer3 == 'да':
            print('Это куб, введите его сторону')
            a = int(input())
            s = a * a * a
            print('Площадь равна', s)
        else:
            print('У фигуры все углы прямые?')
            answer4 = str(input())
            if answer4 == 'да':
                print('Это параллелепипед, введите его длину, ширину и высоту через пробел')
                a, b, c = map(int, input().split())
                s = 2 * (a * b + b * c + a * c)
                print('Площадь равна', s)
            else:
                print('Это пирамида, введите ее периметр основания и апофему через пробел')
                p, l = map(int, input().split())
                s = p * l
                print('Площадь равна', s)