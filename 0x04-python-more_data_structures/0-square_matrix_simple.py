#!/usr/bin/python3
# 1-search_replace.py

def square_matrix_simple(matrix=[]):
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if num_rows > 0 else 0
    result_matrix = []


    for i in range(num_rows):
        
        squared_row = []

        for j in range(num_cols):
            element = matrix[i][j]
            squared_element = element ** 2
            squared_row.append(squared_element)

    
        result_matrix.append(squared_row)

    return result_matrix
