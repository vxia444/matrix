n = int(input())

matrix = []

for i in range(n):
    row = list(map(int, input().split(", ")))
    matrix.append(row)

sum1 = sum(matrix[i][n - i - 1] for i in range(n))

print(sum1)
