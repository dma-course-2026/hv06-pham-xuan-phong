a,b = map(int,input('Nhập 2 số nguyên a,b: ').split())
if a != 0 and b!= 0:
    x = a%b
    y = b%a
    if x == 0 and y != 0:
        print('b là ước của a')
    elif x != 0 and y == 0:
        print('a là ước của b')
    else:
        print('a và b không là ước của nhau')
elif a == 0 and b != 0:
    print('b là ước của a')
elif b == 0 and a != 0:
    print('a là ước của b')
else:
    print('không thỏa mãn')
