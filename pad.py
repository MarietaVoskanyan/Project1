def pad(mat, pad, pad_with=0):
    n_rows = len(mat)
    n_cols = len(mat[0])

    new_mat = [
        [pad_with for col in range(n_cols + pad * 2)]
        for row in range(n_rows + pad * 2)
    ]

    for row in range(n_rows):
        for col in range(n_cols):
            new_mat[row + pad][col + pad] = mat[row][col]

    return new_mat

    mat=(input("Insert matrix: "))
    pad=(input("Insert padding: "))
    print(f'pad(mat, pad)')
