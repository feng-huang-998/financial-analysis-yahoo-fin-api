import moduleYahooFinAPI as finapi
import moduleUtil as util

ticker = "tatt"

tickerQuoteInfo = finapi.getTickerQuoteTable(ticker)
tickerStats = finapi.getTickerStats(ticker)

currentPrice = tickerQuoteInfo["Quote Price"]

marketCap = tickerQuoteInfo["Market Cap"]
marketCap = util.readableToFloat(marketCap)

dividendPerShare = tickerQuoteInfo["Forward Dividend & Yield"].split(" ")[0]
dividendYield = tickerQuoteInfo["Forward Dividend & Yield"].split(" ")[1].replace("(","").replace(")","") 

bookValue = tickerStats[tickerStats.Attribute == "Book Value Per Share (mrq)"].Value

print (tickerQuoteInfo)
print (tickerStats)

print ("currentPrice: " + str(currentPrice))
print ("marketCap: " + str(marketCap))
print ("dividendPerShare: " + str(dividendPerShare))
print ("dividendYield: " + dividendYield)
print ("bookValue: " + bookValue)
