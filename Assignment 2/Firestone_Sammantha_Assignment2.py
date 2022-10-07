# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 13:19:39 2022
COMP-4581 - Algorithms for Machine Learning
Assignment2: Max Stock Profit
@author: Sammy Firestone
"""

import pandas as pd

''' Function to read in csv and export df '''
def readFile(file):
    data = pd.read_csv(file)
    return data

''' Function to filter DF by ticker symbol '''
def filterSymbol(data, symbol):
    filtered_df = data[data['symbol']==symbol]
    return filtered_df

''' Old Testing Stuff for the above functions '''
# df = readFile('prices-split-adjusted.csv')
# secure = readFile('securities.csv')
# filtered = filterSymbol(df, 'AAPL')
# filtered = filtered.reset_index()
# closed = filtered['close'].tolist()
# ticker_list = df['symbol'].unique()

''' Function to calculate the changes between list items '''
def calcChanges(price):
    # create empty list
    changes = []
    # loop threw list and append changes between indexes
    for i in range(len(price)-1):
        delta = round(price[i+1] - price[i],3)
        changes.append(delta)
    return changes

def MSSDAC(A, low=0, high=None):
    # initialize index variables
    leftIndex, rightIndex = None, None
    
    # check for high index
    if high == None:
        high = len(A) - 1
    # check for low index
    if low == high:
        if A[low] > 0:
            # return both value and index
            return A[low], low
        else:
            return 0, None
    #Divide
    # find middle of list
    mid = (low+high)//2
    
    #Conquer
    # recursion on both sides of the list to find max
    maxLeft = MSSDAC(A, low, mid)
    maxRight = MSSDAC(A, mid+1, high)
    
    #Combine
    # set default maxVals
    maxLeft2Center = left2Center = 0
    # iterate threw list to find high price on left side
    for i in range(mid, low-1, -1):
        left2Center += A[i]
        if left2Center > maxLeft2Center:
            # return tuple to get index
            maxLeft2Center, leftIndex = left2Center, i
        #maxLeft2Center = max(left2Center, maxLeft2Center)        
    
    # set default maxVals
    maxRight2Center = right2Center = 0
    # iterate threw list to find high price on right side
    for i in range(mid+1, high+1):
        right2Center += A[i]
        if right2Center > maxRight2Center:
            # return tuple to get index
            maxRight2Center, rightIndex = right2Center, i
        #maxRight2Center = max(right2Center, maxRight2Center)
    
    # find largest profit
    # determine if left side, right side, or in the middle
    largestDiff = max(maxLeft[0], maxRight[0], maxLeft2Center + maxRight2Center)
    if largestDiff == maxLeft[0]:
        return maxLeft
    elif largestDiff == maxRight[0]:
        return maxRight
    else:
        return maxLeft2Center + maxRight2Center, leftIndex, rightIndex


''' More testing above function '''
# changes = calcchanges(closed)
# practice = MSSDAC(changes)

''' Function to get date from index returned by MSSDAC output'''
def getDate(out, data):
    buyDateIndex = out[1]
    sellDateIndex = out[2]
    
    # refer to main DF to get date values
    dates = data['date']
    
    buyDate = dates[buyDateIndex]
    sellDate = dates[sellDateIndex]
    
    return buyDate, sellDate

''' Testing date function '''
# dates = getDate(practice, filtered)

''' Function to get company name from the ticker symbol '''
def getCompany(ticker, data):
    column = data.loc[data['Ticker symbol'] == ticker].iloc[0]
    companyName = column['Security']
    return companyName

''' Testing getCompany function '''
# moretesting = getCompany('AAPL', secure)

''' MAIN FUNCTION!! PUTTING THEM ALL TOGETHER TO GET ALL MAX STOCK PROFITS
    AS WELL AS COMPANY NAME, BUY / SELL DAYS / DATES '''
def MaxStockProfit(priceData, secureData):
    # read in files and get dfs
    priceDF = readFile(priceData)
    secureDF = readFile(secureData)
    
    # get list of all ticker symbols
    ticker_list = priceDF['symbol'].unique() 
    
    # loop threw ticker list to get max stock profit for all!
    for ticker in ticker_list:
        # filter data on ticker symbol
        companyPrices = filterSymbol(priceDF, ticker)
        # reset index so we don't break anything when referring back to that index
        companyPrices = companyPrices.reset_index()
        # convert closing prices to a list for MSSDAC function
        priceChanges = calcChanges(companyPrices['close'].tolist())
        # big boy function-- doing all the heavy lifting to get
        # maxProfit, buy/sell days
        maxProfit = MSSDAC(priceChanges)
        # calling getDate function to convert days -> dates
        dates = getDate(maxProfit, companyPrices)
        
        buyDate = dates[0]
        sellDate = dates[1]
        company = getCompany(ticker, secureDF)
        print(f"{company} ({ticker}) Profit: {maxProfit[0]} buy on day: {maxProfit[1]} ({buyDate}) and sell on day: {maxProfit[2]} ({sellDate})")
        
# set variables for file names and run the program :) 
priceData = 'prices-split-adjusted.csv'
secureData = 'securities.csv'
MaxStockProfit(priceData, secureData)