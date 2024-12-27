# Треугольник Паскаля (сколько столбцов/ строк)

def com(n, k):
    if k == 0 :
        return 1
    if k == n:
        return 1
    return com(n - 1, k - 1) + com(n - 1, k)

# Увеличивается количество колон (строк) на один
def pascals_triangle_rows(rows):
    for i in range( rows):
        result = ""
        for colon in range( i + 1):
            result =result + str(com(i, colon)) + "\t"
        print(result)

def main():
    print('Введите количество строк/столбцов')
    a = int(input())
    res = pascals_triangle_rows(a)
    print('pascals_triangle_rows(',a,')=',res)
    


if __name__=='__main__':
    main()

