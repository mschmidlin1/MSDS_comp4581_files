


def cPairDist(points):
    points = sorted(points)
    return recCPairDist(points)


def recCPairDist(points):
    if len(points)==2:
        return points[1]-points[0]
    if len(points)==3:
        return min(points[2]-points[1], points[1]-points[0])
    
    mid = len(points)//2
    left = points[:mid]
    right = points[mid:]

    return min(recCPairDist(left), recCPairDist(right), points[mid]-points[mid-1])

def main():
    l1 = [7, 4, 12, 14, 2, 10, 16, 6]
    print(f"The shortest distance in {l1} is {cPairDist(l1)}.")

    l2 = [7, 4, 12, 14, 2, 10, 16, 5]
    print(f"The shortest distance in {l2} is {cPairDist(l2)}.")

    l3 = [14, 8, 2, 6, 3, 10, 12]
    print(f"The shortest distance in {l3} is {cPairDist(l3)}.")


if __name__=="__main__":
    main()