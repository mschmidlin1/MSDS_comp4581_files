import pandas as pd
import numpy as np
import math

def loadInvestments(fname):
    df = pd.read_csv(fname)
    df = df[['RegionName', '2019-01', '2020-01']]
    df=df.iloc[1:]
    df = df.reset_index().drop(columns=['index'])
    df['roi'] = df['2020-01'] - df['2019-01']
    df.rename(columns={'2020-01': 'cost'}, inplace=True)
    df.drop(columns=['2019-01'], inplace=True)
    options = df.values.tolist()
    options = sorted(options, key=lambda x: x[1])
    return options


def optimizeInvestments(options, total, step):
    options = np.array(options)
    names = options[:,0]
    costs = options[:,1]
    ROIs = options[:,2]
    names = np.insert(names, 0, 'None')
    costs = np.insert(costs, 0, 0)
    ROIs = np.insert(ROIs, 0, 0)

    string_step = str(step)
    num_zeros = string_step.count('0')

    n = len(options)
    table = [[0 for x in range(0,total + 1, step)] for x in range(n)]



    for i in range(n):
        for j in range(0, total + 1, step):
            if i==0 or j==0:
                continue
            elif i==1:
                if costs[i]<=j:
                    table[i][j]=ROIs[i]
            elif costs[i]>j:
                table[i][j]=table[i-1][j]
            else:

                leftover_funds = j-costs[i]
                leftover_funds = leftover_funds/step
                leftover_funds = math.floor(leftover_funds)
                leftover_funds = int(leftover_funds*step)
                table[i][j] = max(ROIs[i] + table[i-1][leftover_funds] , table[i-1][j])



    maxProfit=table[-1][-1]
    investments=None
    return maxProfit, investments















def main():
    options = loadInvestments("Assignment 3/Metro.csv")
    print(options[:4])

if __name__=="__main__":
    main()