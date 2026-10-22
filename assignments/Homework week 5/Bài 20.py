print('Phương trình bậc 2: ax^2 + bx + c = 0')
a = int(input('Nhập hệ số a: '))
b = int(input('Nhập hệ số b: '))
c = int(input('Nhập hệ số c: '))
d = b**2-4*a*c
if d >= 0:
    e = d**0.5
    f = (-b-e)/(2*a)
    g = (-b+e)/(2*a)
    print('Nghiệm của phương trình là:',f,'và',g)
else:
    print('Phương trình vô nghiệm')
