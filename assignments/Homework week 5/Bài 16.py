a,b,c = map(int,input('Nhập 3 cạnh của một tam giác: ').split())
if a+b>c and b+c>a and a+c>b:
    if a==c or a==b or b==c:
        print('Đó là tam giác cân')
    else:
        print('Đó không là tam giác cân')
else:
    print('Đó không là tam giác')
