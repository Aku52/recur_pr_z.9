# Задача для разбиение числа на сумму слагаемых

def partitions(a, n, k):
    if n:
        for i in range(n+1, 0, -1): # -1 - длина шага 
            if i <= k:
                partitions(a+[i], n-i, i)
    else:
        print( a, end=' , ')
    

def main():
    print('Введите задачу для разбиение числа на сумму слагаемых')
    n = int(input())
    partitions([], n, n)


if __name__=='__main__':
    main()
