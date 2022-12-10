# Find the size of the matrix
# if size is 1x1 then return element 0,0
# if 2x2 = a*d - b*c
# if NxN then a * sign * det(a_minor) + b * sign * det(b_minor) ...
# sign is positive when odd negative when even


def findMatrixDeterminant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]

    elif len(matrix) == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[1][0] * matrix[0][1])

    else:
        determ = 0
        for i in range(len(matrix)): # for each element in the first row
            minor_m = [row[:i] + row[i+1:] for row in (matrix[:0]+matrix[0+1:])] # find the minor matrix(0,i) meaning all values excluding 0th row and i-th column
            determ += (matrix[0][i] * findMatrixDeterminant(minor_m) * (-1)**(i%2)) 
    return determ
        
