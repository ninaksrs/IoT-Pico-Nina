f=[]
count=0
for i in range(101):
    if i in [3,7,8]:
        count+=1
        continue
    if str(i)[-1] in ['3','7','8']:
        count+=1
        continue
    f.append(i)
    print(i)
print('is',sum(f))
print(f'count:{count}')