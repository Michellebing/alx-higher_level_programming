#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    square_one = [[y**2 for y in row]for row in matrix]
    return square_one
