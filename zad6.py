n = int(input())
matrix = []

for _ in range(n):
    row = list(map(int, input().split(', ')))
    matrix.append(row)


sum1 = 0
for i in range(n):
    for j in range(i + 1):
        sum1 += matrix[i][j]

print(sum1)