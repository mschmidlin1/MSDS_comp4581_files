import numpy as np


def prices_to_changes(prices):
    prices = np.array(prices)
    copy_prices = np.copy(prices)
    prices = np.insert(prices, 0, 0)
    copy_prices = np.append(copy_prices, 0)

    changes = copy_prices-prices
    return changes[1:-1]


def maxProfit_Algo(A):
    """
    Takes an array of stock prices and returns the optimal (max profit) buy and sell index positions as a tuple.
    """
    if len(A)==1:
        return 0, 0, A[0]
    
    if len(A)==2:
        both = np.sum(A)

        all_profits = np.array([A[0], A[1], both])
        starts = [0,1,0]
        ends = [0,1,1]

        for i in range(len(all_profits)):
            if sum(all_profits[i]>=all_profits)==3:
                return starts[i], ends[i], all_profits[i]

        raise ValueError("You didn't think of one of the scenarios. (len of 2)")

    if len(A)==3:
        l = A[0]
        m = A[1]
        r = A[2]

        lm = l+m
        lmr = l+m+r
        mr = m+r

        all_profits = np.array([l,m,r,lm,lmr,mr])
        starts = [0,1,2,0,0,1]
        ends = [0,1,2,1,2,2]

        for i in range(len(all_profits)):
            if sum(all_profits[i]>=all_profits)==6:
                return starts[i], ends[i], all_profits[i]
        
        raise ValueError("You didn't think of one of the scenarios. (len of 3)")

    mid=len(A)//2

    l_start, l_end, l_profit = maxProfit_Algo(A[:mid])
    r_start, r_end, r_profit = maxProfit_Algo(A[mid:])
    r_start += mid
    r_end += mid

    m_l_start, m_l_profit = mid-1, A[mid-1]
    m_l_cumsum = A[mid-1]
    for i in range(len(A[:mid])-2, -1, -1):
        if (m_l_cumsum+A[i])>m_l_profit:
            m_l_profit = m_l_cumsum+A[i]
            m_l_start = i
        m_l_cumsum += A[i]

    m_r_end, m_r_profit = mid, A[mid]
    m_r_cumsum = A[mid]
    for i in range(mid+1, len(A)):
        if (m_r_cumsum + A[i])>m_r_profit:
            m_r_profit = m_r_cumsum + A[i]
            m_r_end = i
        m_r_cumsum += A[i]

    m_profit = m_l_profit+m_r_profit
    
    if l_profit>=r_profit and l_profit>=m_profit:
        return l_start, l_end, l_profit
    elif r_profit>=l_profit and r_profit>=m_profit:
        return r_start, r_end, r_profit
    elif m_profit>=l_profit and m_profit>=r_profit:
        return m_l_start, m_r_end, m_profit
    else:
        raise ValueError("You didn't think of one of the scenarios.")


def maxProfit(prices):

    A = prices_to_changes(prices)

    start, end, profit = maxProfit_Algo(A)
    profit = round(profit, 6)

    if profit<=0.0:
        return 0,0,0

    return start, end+1, profit #add 1 to end to convert from "difference array" to "actual prices array"

def main():
    pass

if __name__=="__main__":
    main()