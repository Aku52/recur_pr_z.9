
# Делаем через остаток (в целом в этом заключается весь признак Евклида)
def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)
    
def main():
    print('Ввeдите числа, у которых будем искать НОД')
    a = int(input())
    b = int(input())
    res_num = gcd(a,b)
    print ('gcd(',a,',',b,') =',res_num)
    


if __name__=='__main__':
    main()



