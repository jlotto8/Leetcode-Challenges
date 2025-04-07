"""
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

Example 1:
Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.

Example 2:
Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8

Example 3:
Input: mat = [[5]]
Output: 5

Constraints:
n == mat.length == mat[i].length
1 <= n <= 100
1 <= mat[i][j] <= 100

I: mat,  a  square a matrix
O: int, sum  of matrix diagonals
C: square,  no more than 100 length, each list  no more than 100, not empty
E: a square of 1, a matrix of all the same numbers

Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.

Pseudocode/plan

look at the matrix, at the diaganol rows
sum all the numbers in the first diagonal - left to right
look at the numbers in the second diagonal
if any are the same as the numbers from the first diagonal, ignore them
continue to add to the sum of the fist diagonal with numbers in the second diagonal
return the sum
nested loops

start an accumultor to keep track of the running total sum
loop through the first list
    loop through the nested list to get each item


total_sum = 0 
for i in len(range(mat)):
    for j in len(range(mat)):
        if mat[j] != mat[i]
            total_sum += mat[j]
"""

# def diagonalSum(mat):
mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]

# mat = [[1,2,3],[4,5,6],[7,8,9]]

