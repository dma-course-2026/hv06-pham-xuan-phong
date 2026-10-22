res=1
a = int(input('Nhập cơ số a:'))
n = int(input('Nhập số mũ n:'))
for i in range(1,n+1):
    res *=a
print('a^n=',res)
