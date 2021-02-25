import moduleYahooFinAPI as finapi

ticker = "amzn"

tickerQuoteInfo = finapi.getTickerQuoteTable(ticker)
tickerStats = finapi.getTickerStats(ticker)

currentPrice = tickerQuoteInfo["Quote Price"]

marketCap = tickerQuoteInfo["Market Cap"]
if marketCap.endswith("T"):
    marketCap = float(marketCap[:-1]) * 1000000000000 
elif marketCap.endswith("B"):
    marketCap = float(marketCap[:-1]) * 1000000000
elif marketCap.endswith("M"):
    marketCap = float(marketCap[:-1]) * 1000000
else: 
    marketCap = float(marketCap[:-1])

dividendPerShare = tickerQuoteInfo["Forward Dividend & Yield"].split(" ")[0]
dividendYield = tickerQuoteInfo["Forward Dividend & Yield"].split(" ")[1].replace("(","").replace(")","")

print ("tickerQuoteInfo: " + tickerQuoteInfo)
print ("tickerStats: " + tickerStats)

print ("currentPrice: " + str(currentPrice))
print ("marketCap: " + str(marketCap))
print ("dividendPerShare: " + str(dividendPerShare))
print ("dividendYield: " + dividendYield)

