num = int(input())
matrix = []

for i in range(num):
    matrix.append([])
    for j in range(num):
        matrix[i].append(j + 1 + i * num)

sums = [sum(row) for row in matrix]

for row_sum in sums:
    print(row_sum)