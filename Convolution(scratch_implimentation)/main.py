KROW = 3
KCOL = 3


def input_mat(matrix,row,col):
    print("Enter the elemnts of", matrix)
    for i in range(row):
        row_input = list(map(int, input().split()))
        if len(row_input) != col:
            print("Invalid number of elements in row. Please enter", col, "elements separated by spaces.")
            return None
        matrix.append(row_input)
    return matrix

def convolute_mat(matrix,kernel):
    input_row = len(matrix)
    input_col = len(matrix[0])
    kernel_row = len(kernel)
    kernel_col = len(kernel[0])

    result_col = input_col - kernel_col + 1
    result_row = input_row - kernel_row + 1
    print(f"No of rows in matrix: {input_row}\nNo of col in matrix: {input_col}\nNo of rows in kernel: {kernel_row}\nNo of col in Kernel: {kernel_col}")

    result = [[0 for _ in range(result_col)]for _ in range(result_row)]

    for i in range(result_row):
        for j in range(result_col):
            for k in range(kernel_row):
                for l in range(kernel_col):
                    result[i][j] += matrix[i+k][j+l] * kernel[k][l]

    return result

def print_mat(result):
    for row in result:
        print(*row)


def main():
    matrix = []
    kernel = []

    while True:
        key = input("Press Enter to continue or Q to quit: ")

        if key == 'q':
            break
        else:
            Mrow = int(input("Enter the number of rows: "))
            Mcol = int(input("Enter the number of cols: "))

            print()
            input_mat(matrix,Mrow,Mcol)
            print()
            input_mat(kernel,KROW,KCOL)
            print()
            result = convolute_mat(matrix,kernel)
            print()
            print_mat(result)
            matrix.clear()
            kernel.clear()
            result.clear()

main()


# for i in range(len(result)):
#     for j in range(len(result[0])):
#         print(result[i][j], end=" ")
# print()
# for i in range(rows):
#         row = list(map(int, input().split()))
#         if len(row) != cols:
#             print("Invalid number of elements in row. Please enter", cols, "elements separated by spaces.")
#             return None
#         matrix.append(row)
#     return matrix
