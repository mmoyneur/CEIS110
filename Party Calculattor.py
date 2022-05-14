#Part calculator
#name: Michael Moyneur
#date: 8/30/2021
#input
print("welcome to the party calculator")
bannerWidth = float(input("Please enter the banner width"))
bannerLength = float(input("Please enter the banner length"))
costPerSqIn = float(input("Please enter the cost per square inch: "))

#processing
bannerArea = bannerWidth * bannerLength
totalCost = bannerArea * costPerSqIn

#output
print("your total cost is ", totalCost)