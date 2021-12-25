from random import randint

num_in_group = 1
n = num_in_group + 3
m = num_in_group + 2


matrix = [[randint(1, 10) for j in range(m)] for i in range(n)]

for line in matrix:
    print('   '.join(map(str, line)))