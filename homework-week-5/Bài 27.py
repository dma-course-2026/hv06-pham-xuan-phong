a,b,c,d,e = map(float,input('Nhập 5 số bất kì: ').split())
f = min(a,b,c,d,e)
if f == a:
    print('Số bé nhất trong 5 số là: ', a)
elif f == b:
     print('Số bé nhất trong 5 số là: ', b)
elif f == c:
     print('Số bé nhất trong 5 số là: ', c)
elif f == d:
     print('Số bé nhất trong 5 số là: ', d)
else:
     print('Số bé nhất trong 5 số là: ', e)
