price=int(input(' Price:'))
discount=0
if price>=1 and price<=100000:
    discount=0.02
elif price>=100001 and price<=200000:
    discount=0.03
elif price>=200001 and price<=500000:
    discount=0.05
else:
    discount=0.07
discount_price=price*discount
Total=price-discount_price
print(f'price is {price}')
print(f'discount is {discount}={discount_price}')
print(f'Total is {Total}')
print('Thank you for using')