from time import time


# Algorithm 1: Divide-and-Conquer
def DACcoins(coins, amount):
    if amount == 0: # The base case
        return 0
    else: # The recursive case
        minCoins = float("inf")
    for currentCoin in coins: # Check all coins
    # If we can give change
        if (amount - currentCoin) >= 0:
        # Calculate the optimal for currentCoin
            currentMin = DACcoins(coins, amount-currentCoin) + 1
            # Keep the best
            minCoins = min(minCoins, currentMin)
    return minCoins


# Algorithm 2: Dynamic Programming with Traceback
def DPcoins(coins, amount):
    ncoins=[0,1,2,3,4,1]
    cointypes=[0,1,1,1,1,5]
    if amount>5:
        for i in range(6, amount+1):
            temp=[]
            for coin in coins:
                if i-coin<0:
                    temp.append(float("inf"))
                else:
                    temp.append(ncoins[i-coin])
            min_val=min(temp)
            min_index=temp.index(min_val)
            ncoins.append(min_val+1)
            cointypes.append(coins[min_index])
    
    to_return=[]
    i=amount
    while i>0:
        to_return.append(cointypes[i])
        print(cointypes[i])
        i-=cointypes[i]

    return ncoins[amount]










def main():
    C = [1,5,10,12,25] # coin denominations (must include a penny)
    A = int(input('Enter desired amount of change: '))
    assert A>=0
    print("DAC:")
    t1 = time()
    numCoins = DACcoins(C,A)
    t2 = time()
    print("optimal:",numCoins," in time: ",round((t2-t1)*1000,1),"ms")
    print()
    print("DP:")
    t1 = time()
    numCoins = DPcoins(C,A)
    t2 = time()
    print("optimal:",numCoins," in time: ",round((t2-t1)*1000,1),"ms")

if __name__=="__main__":
    main()