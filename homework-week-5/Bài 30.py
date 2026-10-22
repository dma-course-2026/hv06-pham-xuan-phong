n = int(input('Nhập số giây: '))
g = n//3600
p = (n-g*3600)//60
giay = (n-g*3600-p*60)
print('Vậy',n,'giây tương ứng với',g,'giờ',p,'phút',giay,'giây')
