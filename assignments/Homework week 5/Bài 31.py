h,m,s = map(int,input('Nhập lần lượt giờ,phút,giây: ').split())
if s == 59:
    if m == 59:
        if h == 23:
            print('Giờ hiện tại là: 00  00  00')
        else:
            h += 1
            print('Giờ hiện tại là:',h,' ','00',' ','00')
    else:
        m += 1
        print('Giờ hiện tại là:',h,' ',m,' ','00')
else:
    s += 1
    print('Giờ hiện tại là:',h,' ',m,' ',s,' ')
