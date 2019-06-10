a = int(input('Enter number: '))

k=0

for i in range(2, a):
    if (a % i == 0):
        k=1
        break


if (k==0):
    print('Number is Prime!')
else:
    print("Number is not prime!")