print('Nhập tọa đô tâm và bán kính của đường tròn:')
print('Nhập tọa độ tâm của đường tròn:')
x = float(input('x='))
y = float(input('y='))
print('Nhập bán kính của đường tròn:')
R = float(input('R='))
print('Chọn điểm A(a,b)')
a = float(input('a='))
b = float(input('b='))
d = ((a-x)**2+(b-y)**2)**0.5
if d < R :
    print('Điểm A nằm trong đường tròn')
elif d == R:
    print('Điểm A nằm trên đường tròn')
else:
    print('Điểm A nằm ngoài đường tròn')
