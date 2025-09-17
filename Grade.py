score=int(input('Enter Score:'))
grade=''
if score>=90 and score<=100:
    grade='A'
elif score>=80 and score<=89:
    grade='B'
elif score>=70 and score<=79:
    grade='C'
elif score>=60 and score<=69:
    grade='D'
elif score>=50 and score<=59:
    grade='F'
else:
    grade='I'
print("Your grade is :",grade)

