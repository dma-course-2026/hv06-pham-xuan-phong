print('Ta có hệ phương trình bậc nhất 2 ẩn là: Ax+By=M và Cx+Dy=N')
A = float(input('Nhập hệ số A: '))
B = float(input('Nhập hệ số B: '))
M = float(input('Nhập hệ số M: '))
C = float(input('Nhập hệ số C: '))
D = float(input('Nhập hệ số D: '))
N = float(input('Nhập hệ số N: '))
Det = A*D-B*C
Dx = M*D-B*N
Dy = A*N-M*C
if Det != 0:
    print('Nghiệm của hệ phương trình là: ', Dx/Det)
    print('Nghiệm của hệ phương trình là: ', Dy/Det)
elif Det == 0 and  Dx == Dy == 0:
    print('Hệ phương trình có vô số nghiệm')
else:
    print('Hệ phương trình vô nghiệm')
