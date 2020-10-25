# Sudoku

This program can solve every Sudoku with a systematic approach. For this, a 3-dimensionallys array is created. The first two dimensions contain the sudoku (either the given number of the cell, or in case the cell is still emtpy, the value 0). The third dimension contains all possible solutions of the given field, considering, that only numbers that are not already in the same row, column or square are possible solution. 
In a first step, all possible solutions of each field are written into the third dimension of that field. In a second step, the program iterates through all the fields and checks the possible solutions. if there is only one possible solution for a given field, the value is written into the cell. If there is a possible solution for a given field, that is not possible for any other field within the same row, column, or square, then write this value into the given cell. 
Continue these steps, until all there are no empty cells anymore.
.
