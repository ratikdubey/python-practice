name = input('Student Name: ')

roll_no = input('Roll Number: ')

marks = []
for i in range(5):
    mark = int(input('Enter subject mark: '))
    marks.append(mark)

total = 0
for item in marks:
    total += item

percent = (total/500) * 100

if percent > 90:
    print('Grade is A+')
elif percent >= 80:
    print('Grade is A')
elif percent >= 70:
    print('Grade is B+')
elif percent >= 60:
    print('Grade is B')
elif percent >= 50:
    print('Grade is C')
else:
    print('Fail!')