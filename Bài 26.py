a,b,c,d = map(int,input('Nhập 4 số nguyên a,b,c,d theo thứ tự: ').split())
e = max(a,b,c,d)
if e == a:
    print('Số lớn nhất trong 4 số là: ',a)
elif e == b:
    print('Số lớn nhất trong 4 số là: ',b)
elif e == c:
    print('Số lớn nhất trong 4 số là: ',c)
else:
    print('Số lớn nhất trong 4 số là: ',d)
