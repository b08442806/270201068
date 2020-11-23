cover_price= float(24.95)
discount=float(input("indirim miktarı"))/100
cover_price2= float(cover_price-(cover_price*discount))
first_copy= int(3)
copy_price= float(0.75)
total_copy=(60)
x= float(cover_price2*total_copy+(copy_price*(total_copy-1)+first_copy))
print(x)