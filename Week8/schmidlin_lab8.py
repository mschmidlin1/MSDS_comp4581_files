





def parenStr(traceback, mats, start_mat, end_mat):

    if len(mats)==2:
        return f'({mats[0]}*{mats[1]})'
    if len(mats)<2:
        return mats[0]

    div = traceback[start_mat][end_mat]
    left = mats[:div+1]
    right = mats[div+1:]

    left_str = parenStr(traceback, mats=left, start_mat=start_mat, end_mat=div)

    traceback = traceback[div+1:]
    new_traceback = []
    for row in traceback:
        row = row[div+1:]
        new_row = []
        for i in row:
            if i == None:
                new_row.append(None)
            else:
                new_row.append(i-(div+1))
        new_traceback.append(new_row)
    
    right_str = parenStr(new_traceback, mats=right, start_mat=0, end_mat=end_mat-(div+1))

    ret_str = '('+left_str + right_str+')'
    return ret_str







def printMatrix(m):
    for row in m:
        print(row)
def chainMatrix(dims):
    # Create the empty 2-D table
    n = len(dims)-1
    m = [[None for i in range(n)] for j in range(n)]
    traceback = [[None for i in range(n)] for j in range(n)]
    # Fill in the base case values
    for i in range(n):
        m[i][i] = 0
    # Fill in the rest of the table diagonal by diagonal
    for chainLength in range(2,n+1):

        for i in range(n+1-chainLength):
            j = i + chainLength - 1
            # Fill in m[i][j] with the best of the recursivme options
            m[i][j] = float("inf")
            for k in range(i,j):
                # Two previous table values plus
                # what it cost to mult the resulting matrices
                q = m[i][k]+m[k+1][j]+dims[i]*dims[k+1]*dims[j+1]
                if q < m[i][j]:
                    m[i][j] = q
                    traceback[i][j] = k
    
    
    # printMatrix(traceback)
    printMatrix(m)

    mats = ['A0', 'A1', 'A2', 'A3', 'A4', 'A5']
    start_mat = 0
    end_mat = 5
    print(parenStr(traceback, mats, start_mat, end_mat))
    return m[0][n-1]














def main():
    dims = [30,35,15,5,10,20,25]
    print(chainMatrix(dims))

if __name__=="__main__":
    main()