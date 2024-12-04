
def input_Dim():
    M_row = int(input("Enter the number of rows: "))
    M_col = int(input("Enter the number of cols: "))

    return M_row,M_col

def input_mat(matrix,M_row,M_col,key):
    print(f"Enter the elements of matrix {key}: ")

    for i in range(M_row):
        row_input = list(map(int, input().split()))
        if len(row_input) != M_col:
            print("Invalid number of elements in row.Please enter",M_col,"elements seperated by spaces")
            return None
        else:
            matrix.append(row_input)
    return matrix


def matmul(X,Y,result):
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(X[0])):
                result[i][j] += X[i][k] * Y[k][j]
    return result

def print_mat(result):
    for row in result:
        print(*row)





def main():
    X = []
    Y = []
    result = []

    while True:
        
        key = input("Press Enter to Proceed or Q to quit: ")

        if key == 'q':
            break
        else:
            X_row,X_col = input_Dim()
            print()
            Y_row,Y_col = input_Dim()
            print()
            result = [[0 for _ in range(Y_col)]for _ in range(X_row)]
            X = input_mat(X,X_row,X_col,1)
            print()
            Y = input_mat(Y,Y_row,Y_col,2)
            print()
            result = matmul(X,Y,result)
            print("The result matrix is: ")
            print_mat(result)
            print()
            X.clear()
            Y.clear()
            result.clear()


main()

# X = [[2, 7, 4],[5, 1, 8 ],[3, 6, 9]]

# Y = [[9, 2, 5, 7],[4, 6, 1, 3],[8, 3, 2, 5]]

# result = [[0,0,0,0],
#          [0,0,0,0],
#          [0,0,0,0]]

# print(len(Y[0]))

# for i in range(len(X)):
#     for j in range(len(Y[0])):
#         for k in range(len(X[0])):
#             result[i][j] += X[i][k] * Y[k][j]


# print(result) 