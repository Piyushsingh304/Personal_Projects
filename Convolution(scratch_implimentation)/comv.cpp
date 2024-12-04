
#include <iostream>
#include <vector>

using namespace std;

// Function to perform 2D convolution
vector<vector<int>> convolution(const vector<vector<int>>& input_matrix, const vector<vector<int>>& kernel) {
    int input_rows = input_matrix.size();
    int input_cols = input_matrix[0].size();
    int kernel_rows = kernel.size();
    int kernel_cols = kernel[0].size();
    
    int result_rows = input_rows - kernel_rows + 1;
    int result_cols = input_cols - kernel_cols + 1;
    
    vector<vector<int>> result(result_rows, vector<int>(result_cols, 0));

    // Convolution operation
    for (int i = 0; i < result_rows; ++i) {
        for (int j = 0; j < result_cols; ++j) {
            for (int k = 0; k < kernel_rows; ++k) {
                for (int l = 0; l < kernel_cols; ++l) {
                    result[i][j] += input_matrix[i+k][j+l] * kernel[k][l];
                }
            }
        }
    }

    return result;
}

int main() {
    // Define the input matrix
    vector<vector<int>> input_matrix = {
        {41, 29, 13, 27, 5, 39},
        {11, 34, 30, 20, 35, 18},
        {24, 3, 48, 9, 32, 36},
        {22, 37, 16, 19, 26, 17},
        {46, 1, 12, 7, 43, 14},
        {4, 8, 31, 2, 28, 42},
        {25, 47, 10, 38, 21, 15},
        {45, 23, 6, 44, 40, 33}
    };

    // Define the kernel
    vector<vector<int>> kernel = {
        {1, 0, 1},
        {0, 1, 0},
        {1, 0, 1}
    };

    // Perform convolution
    vector<vector<int>> result = convolution(input_matrix, kernel);

    // Print the result
    cout << "Convolution result:" << endl;
    for (int i = 0; i < result.size(); ++i) {
        for (int j = 0; j < result[0].size(); ++j) {
            cout << result[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}
