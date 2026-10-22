a = float(input("Nhập tiền điện:"))
if a <= 60:
    print("Tiền điện tháng này là:", 60*a)
elif 60 < a <= 160:
    print('Tiền điện tháng này là:', 8*(a-60)+300)
elif 160 < a:
    print('Tiền điện tháng này là:', 1100+10*(a-160))
