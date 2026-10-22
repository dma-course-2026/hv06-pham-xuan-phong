a = int(input('Nhập số có 3 chữ số:'))
b = a//100
c = (a-(a//100)*100)//10
d = a-(a//100)*100-((a-(a//100)*100)//10)*10
print('Hàng trăm:',b,'Hàng chục:',c,'Hàng đơn vị:',d)
