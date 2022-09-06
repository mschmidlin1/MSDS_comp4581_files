
def main():
    print("hello world")



def dot(X, Y):
    if len(X) != len(Y):
        raise TypeError('Cannot do dot of arrays of different length.')
    total = 0
    for x, y in zip(X, Y):
        total += x*y
    return total

def row(M, index):
    return M[index]

def column(M, index):
    col = []
    for row in M:
        col.append(row[index])
    return col


def printMatrix(m): 
    for row in m:
        print(row)

def matrixMult(A, B):

    shape_A = (len(column(A, 0)), len(row(A, 0)))
    shape_B = (len(column(B, 0)), len(row(B, 0)))

    if shape_A[1] != shape_B[0]:
        print(f"Cannot multiply matrices of dimension {shape_A} and {shape_B}.")
        return None
    
    result_matrix = []
    for i in range(shape_A[0]):
        r = []
        for j in range(shape_B[1]):
            r.append(dot(row(A, i), column(B, j)))
        result_matrix.append(r)

    return result_matrix





if __name__=="__main__":
    main()