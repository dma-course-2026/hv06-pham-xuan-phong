a,b,c = map(float,input().split())
d = (a+b+c)/3
print('Điểm trung bình là:',d)
if d >= 5.0:
    print("Đã đỗ")
else:
    print('Đã trượt')
