def get_matrix(n, m, value) :
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            j = matrix[i]
            j.append(value)
    print(matrix)
get_matrix(10,1,1)
