
def readableToFloat(humanNumber): 
    if humanNumber.endswith("T"):
        return float(humanNumber[:-1]) * 1000000000000 
    elif humanNumber.endswith("B"):
        return float(humanNumber[:-1]) * 1000000000
    elif humanNumber.endswith("M"):
        return float(humanNumber[:-1]) * 1000000
    else: 
        return float(humanNumber[:-1])
