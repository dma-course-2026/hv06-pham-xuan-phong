a = int(input('Nhập chiều dài sân:'))
b = int(input('Nhập chiều rộng sân:'))
c = b/2
d = a*b -(c**2)*3.14
if a > b:
    print('Diện tích còn lại là:',d)
else:
    print('Yêu cầu nhập lại chiều dài lớn hơn chiều rộng')
