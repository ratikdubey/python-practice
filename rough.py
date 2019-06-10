# Function to solve Towers of Hanoi problem

def towers_of_hanoi(n, from_rod, int_rod, to_rod):

    if n == 1:
        print('Disk {} moves from {} to {}'.format(n, from_rod, to_rod))
        return

    else:
        towers_of_hanoi(n-1, from_rod, to_rod, int_rod)
        print('Disk {} moves from {} to {}'.format(n, from_rod, to_rod))
        towers_of_hanoi(n-1, int_rod, from_rod, to_rod)

input = int(input('Enter number of disks: '))

towers_of_hanoi(input, 'A', 'B', 'C')