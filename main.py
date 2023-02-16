#########################
# CSCI 1380.04
# Spring 2022
# Lab 07
# Eduardo Salinas
#########################

# Declares variable {matrix} to have a nested list within a list
matrix = [[6, -9],[1, 5]]

# Declares variable {determinant_result} as the determinant of the variable {matrix}
determinant_result = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

# Displays into console a message alongside the variable {determinant_result}
print(f"The determinant of the matrix is {determinant_result}")