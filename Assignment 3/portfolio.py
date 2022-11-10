from inspect import trace
import pandas as pd
import numpy as np
import math
import time

def loadInvestments(fname):
    df = pd.read_csv(fname)
    df = df[['RegionName', '2019-01', '2020-01']]
    df=df.iloc[1:]
    df = df.reset_index().drop(columns=['index'])
    df['roi'] = df['2020-01'] - df['2019-01']
    df.rename(columns={'2020-01': 'cost'}, inplace=True)
    df.drop(columns=['2019-01'], inplace=True)
    options = df.values.tolist()
    # options = sorted(options, key=lambda x: x[1])
    return options

def traceback(dp_table, step, costs):

    if dp_table.shape[0]<2 or dp_table.shape[1]<2:
        return []

    options = []
    if dp_table[-1][-1] != dp_table[-2][-1]:
        options.append(len(dp_table)-1)
        col_num = dp_table.shape[1]-1
        total_amount = col_num*step
        leftover_funds=total_amount-costs[-1]

        leftover_funds = leftover_funds/step
        new_last_col = int(math.floor(leftover_funds))
        options += traceback(dp_table[:-1,:new_last_col+1], step, costs[:-1])
    else:
        options += traceback(dp_table[:-1,:], step, costs[:-1])

    return options

def optimizeInvestments(options, total, step):
    names = [x[0] for x in options]
    costs = [x[1] for x in options]
    ROIs = [x[2] for x in options]
    names = np.array(names)
    costs = np.array(costs)
    ROIs = np.array(ROIs)
    names = np.insert(names, 0, 'None')
    costs = np.insert(costs, 0, 0)
    ROIs = np.insert(ROIs, 0, 0)

    string_step = str(step)
    num_zeros = string_step.count('0')

    n = len(options)
    table = [[0 for x in range(int(total/step) + 1)] for x in range(n+1)]



    for i in range(n+1):
        for j in range(int(total/step) + 1):
            if i==0 or j==0:
                continue
            elif i==1:
                if costs[i]<=(j*step):
                    table[i][j]=ROIs[i]
            elif costs[i]>(j*step):
                table[i][j]=table[i-1][j]
            else:

                leftover_funds = (j*step)-costs[i]
                leftover_funds = leftover_funds/step
                leftover_funds = int(math.floor(leftover_funds))
                table[i][j] = max(ROIs[i] + table[i-1][leftover_funds] , table[i-1][j])
    
    dp_table = np.array(table)
    investments = traceback(dp_table, step, costs)




    investment_names = [names[i] for i in investments]
    maxProfit=table[-1][-1]
    return maxProfit, investment_names
















def main():
    
    options = loadInvestments("Assignment 3/Metro.csv")
    # for op in options[:5]:
    #     print(op)
    start_time = time.perf_counter()
    max_profit, investment_names = optimizeInvestments(options, 1000000, 1000)

    end_time = time.perf_counter()
    print(f"Calculations done in {(end_time-start_time):0.4f} seconds")
    print(max_profit)
    print(investment_names)
if __name__=="__main__":
    main()