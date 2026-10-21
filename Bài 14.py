a,b,c = map(int,input().split())
p = (a+b+c)/2
S = (p*(p-a)*(p-b)*(p-c))**0.5
P = p*2
if a+b > c and  b+c>a and a+c>b :
    print('Diện tích tam giác đó là:', S)
    print('Chu vi tam giác đó là:', P)
else:
    print('Ba số đó không tạo thành một tam giác')
