import math
import random
from time import time

def isPrime(p):
    sqrt_p = math.floor(math.sqrt(p))

    for i in range(2, sqrt_p+1):
        if p%i==0:
            return False
    return True

def nBitPrime(n):
    while True:
        rand_float = random.random()
        num = rand_float*(2**n)
        num = math.floor(num)
        if num>=2 and isPrime(num):
            return num

def factor(n):
    
    first_num=None
    for i in range(2, n):
        if n%i==0:
            first_num=i
            break
    second_num=int(n/first_num)
    return set([first_num, second_num])







def main():
    print()
    print("-"*50)
    print("This program will run forever,")
    print("If you wish to quit, press 'Ctrl+c'")
    print("-"*50)
    with open('decryption_time1.csv', 'w') as f:
        f.write("Num Encryption bits,Decryption time (ms)\n")
    print()
    print("Num Encryption bits \t\t\t Decryption time (ms)")
    n=15
    while True:
        pq = nBitPrime(n)*nBitPrime(n)
        t1 = time()
        factor(pq)
        t2 = time()
        t = (t2-t1)*1000

        print(f"{n} \t\t\t\t\t {t}")
        with open('decryption_time1.csv', 'a') as f:
            f.write(f"{n},{t}\n")
        n+=1









if __name__=="__main__":
    main()