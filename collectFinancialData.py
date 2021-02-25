import moduleYahooFinAPI as finapi

ticker = "amzn"

tickerQuoteInfo = finapi.getTickerQuoteTable(ticker)
tickerStats = finapi.getTickerStats(ticker)
print (tickerQuoteInfo)
print (tickerStats)

currentPrice = tickerQuoteInfo["Quote Price"]
print ("currentPrice: " + str(currentPrice))

marketCap = tickerQuoteInfo["Market Cap"]
if marketCap.endswith("T"):
    marketCap = float(marketCap[:-1]) * 1000000000000 
elif marketCap.endswith("B"):
    marketCap = float(marketCap[:-1]) * 1000000000
elif marketCap.endswith("M"):
    marketCap = float(marketCap[:-1]) * 1000000
else: 
    marketCap = float(marketCap[:-1])
print ("marketCap: " + str(marketCap))

dividendPerShare = tickerQuoteInfo["Forward Dividend & Yield"].split(" ")[0]
dividendYield = tickerQuoteInfo["Forward Dividend & Yield"].split(" ")[1].replace("(","").replace(")","")
print ("dividendPerShare: " + str(dividendPerShare))
print ("dividendYield: " + dividendYield)

