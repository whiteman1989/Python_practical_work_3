num_in_group = 1
n = num_in_group + 3
m = num_in_group + 2

a = [[int(input("Введіть значення для комірки-"+str(j)+" рядку-"+str(i)+": ")) for j in range(m)] for i in range(n)]

print("Матриця:")
for line in a:
    print('   '.join(map(str, line)))