#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        print(' '.join("{:d}".format(j) for j in x))
