
def main():
    print("hello world")



def dot(X, Y):
    if len(X) != len(Y):
        raise TypeError('Cannot do dot of arrays of different length.')
    total = 0
    for x, y in zip(X, Y):
        total += x*y
    return total


def printMatrix(m): 
    for row in m:
        print(row)

def matrixMult(A, B):
    # Your code goes here
    
    
    
    
    pass





if __name__=="__main__":
    main()