tong = 0
print('Nhập 2 số m<n')
m = int(input('Nhập số m='))
n = int(input('Nhập số n='))
if m>=n:
    print('Yêu cầu nhập lại')
else:
    for i in range(m,n+1):
        if i%3==0 or i%5==0:
            tong += i
print('Tổng Các Số Chia Hết Cho 3 Hoặc 5 là:',tong)     
            
    
