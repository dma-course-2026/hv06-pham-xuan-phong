a,b,c = map(int,input('Nhập độ dài 3 cạnh của một tam giác: ').split())
if a+b>c and b+c>a and a+c>b:
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or c**2 + b**2 == a**2:
        print('Đó là tam giác vuông')
    else:
        print('Đó không là tam giác vuông')
else:
    print('Đó không là tam giác')
