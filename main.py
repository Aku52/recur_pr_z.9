# Главный файл

# НОД по Евклида
import Euclid as m1
# Треугольник Паскаля (сколько столбцов/ строк)
import Pascal as m2
# Задача для разбиение числа на сумму слагаемых
import terms as m3

def main():
    print('Введите E, если хотите найти НОД \n'
          'Введите P, если хотите увидеть треугольник Паскаля \n'
          'Введите T, если хотите разбить число на слогаемые :')
    user_1 = input()
    if user_1.upper()== 'E':
        print('Ввeдите числа, у которых будем искать НОД:')
        a = int(input())
        b = int(input())
        print('Ответ:', m1.gcd(a,b))
    elif user_1.upper()== 'P':
        print('Введите количество строк/столбцов, которые вы хотите увидеть')
        a = int(input())
        print('Ответ:', m2.pascals_triangle_rows(a))
    elif user_1.upper()== 'T':   
        print('Введите задачу для разбиение числа на сумму слагаемых')
        n = int(input())
        print('Ответ:')
        m3.partitions([], n, n)
    else:
        print('Задача не понятна')

if __name__=='__main__':
    main()


        
