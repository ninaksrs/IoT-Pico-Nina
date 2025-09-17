n = int(input('Please enter cash amount: '))
denominations = [100, 50, 20, 10, 5, 2, 1]
count_total=0

for b in denominations:
    count = n // b
    if count > 0:
        print(f'${b} : {count}')
        n = n % b
        count_total += count
print('Total',count_total)
    