m = int(input('Nhập số nguyên m: '))
n = int(input('Nhập số nguyên n: '))
a = m-n
e = a%2
if e == 0:
    print('m,n cùng tính chẵn lẻ')
else:
    print('m,n khác tính chẵn lẻ')
