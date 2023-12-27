import math

lb = 1
coinsPerLB = 50

totalOfCoins = lb*coinsPerLB

platinumRatio = 0.0347 # Originally it was 0.0847
goldRatio = 0.327746 # Originally it was 0.5638
electrumRatio = 0.1879333333 # A third part of the original Gold Ratio
silverRatio = 0.3019 # Originally it was 0.2819
copperRatio = 0.1504 # Originally it was 0.0704

platinumAmmount = math.floor(totalOfCoins * platinumRatio)
goldAmmount = math.floor(totalOfCoins * goldRatio)
electrumAmmount = math.floor(totalOfCoins * electrumRatio)
silverAmmount = math.floor(totalOfCoins * silverRatio)
copperAmmount = math.floor(totalOfCoins * copperRatio)

actualAmmount = platinumAmmount + goldAmmount + electrumAmmount + silverAmmount + copperAmmount

print(str(lb) + "lb of coins should have " + str(totalOfCoins) + " coins.")
print(str(platinumAmmount) + "pp")
print(str(goldAmmount) + "gp")
print(str(electrumAmmount) + "ep")
print(str(silverAmmount) + "sp")
print(str(copperAmmount) + "cp")

print("Because of flooring, the actual total of coins is " + str(actualAmmount) + " coins.")


