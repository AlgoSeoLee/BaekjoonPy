from sys import stdin

mixtureType = ['AB', 'BC', 'AC']
materialType = ['A', 'B', 'C']

maximumProfit = 0

numOfCase = int(stdin.readline())

def mixtureCreate(materialQuantity, mixtureCase, targetMixture):
    materialA = targetMixture[0]
    materialB = targetMixture[1]
    materialAQuantity = materialQuantity[materialA]
    materialBQuantity = materialQuantity[materialB]

    if materialAQuantity != 0 && materialBQuantity != 0:
        mixtureCase[targetMixture] += 1
        materialQuantity.update({materialA: materialAQuantity - 1, materialB: materialBQuantity - 1})

for _ in numOfCase:
    materialQuantityOrigin = dict(zip(materialType, stdin.readline().split()))
    mixturePrice = dict(zip(mixtureType, stdin.readline().split()))
    
    mixtureCase = { 'AB': 0, 'BC': 0, 'AC': 0 }
