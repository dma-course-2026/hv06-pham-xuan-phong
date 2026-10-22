a = int(input('Nhập số nguyên a: '))
b = int(input('Nhập số nguyên b: '))
c = input('Nhập phép toán: ')
if c == "+" :
    ketqua1 = a + b
    print(' Đáp án là', ketqua1)
elif c == "-" :
    ketqua2 = a - b
    print('Đáp án là', ketqua2)
elif c == "*" :
    ketqua3 = a*b
    print('Đáp án là', ketqua3)
else:
    if b == 0 :
        print('Yêu cầu nhập lại giá trị b khác 0')
    else:
        ketqua4 = a/b
        print('Đáp án là', ketqua4)
