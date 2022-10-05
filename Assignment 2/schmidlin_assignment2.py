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
        if both>=A[0] and both>=A[1]:
            return 0, 1, both
        elif A[0]>=both and A[0]>=A[1]:
            return 0, 0, A[0]
        elif A[1]>=both and A[1]>=A[0]:
            return 1, 1, A[1]
        else:
            raise ValueError("You didn't think of one of the scenarios. (len of 2)")

    if len(A)==3:
        l = A[0]
        m = A[1]
        r = A[2]

        lm = l+m
        lmr = l+m+r
        mr = m+r

        all_profits = [l,m,r,lm,lmr,mr]

        start, end, profit = None, None, None

        if max(all_profits) in (l,lm,lmr):
            start=0
        elif max(all_profits) in (m, mr):
            start=1
        else:
            return 2,2,r
        
        if max(all_profits) in (lmr, mr):
            end=2
        elif max(all_profits) in (lm, m):
            end=1
        else:
            return 0,0,l
        
        if start==end:
            return 1,1,m
        elif start==0 and end==2:
            return 0,2,lmr
        elif start==0 and end==1:
            return 0,1,lm
        elif start==1 and end==2:
            return 1,2,mr
        else:
            raise ValueError("You didn't think of one of the scenarios. (len of 3)")

    mid=len(A)//2

    l_start, l_end, l_profit = maxProfit_Algo(A[:mid])
    r_start, r_end, r_profit = maxProfit_Algo(A[mid:])

    m_l_start, m_l_profit = mid-1, A[mid-1]
    m_l_cumsum = A[mid-1]
    for i in range(len(A[:mid])-2, -1, -1):
        if (m_l_cumsum+A[i])>m_l_cumsum:
            m_l_profit = m_l_cumsum+A[i]
            m_l_start = i
        m_l_cumsum += A[i]

    m_r_end, m_r_profit = mid, A[mid]
    m_r_cumsum = A[mid]
    for i in range(mid+1, len(A)):
        if (m_r_cumsum + A[i])>m_r_cumsum:
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

    return start, end+1, profit #add 1 to end to convert from "difference array" to "actual prices array"

def main():
    pass

if __name__=="__main__":
    main()