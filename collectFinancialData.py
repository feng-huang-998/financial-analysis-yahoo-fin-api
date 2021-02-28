import moduleYahooFinAPI as finapi
import moduleUtil as util
import datetime

ticker = "amzn"

tickerQuoteInfo = finapi.getTickerQuoteTable(ticker)
tickerStats = finapi.getTickerStats(ticker)
tickerIncomeStatement = finapi.getIncomeStatement(ticker)
tickerBalanceSheet = finapi.getBalanceSheet(ticker)

currentPrice = tickerQuoteInfo["Quote Price"]

marketCap = tickerQuoteInfo["Market Cap"]
marketCap = util.readableToFloat(marketCap)

dividendPerShare = tickerQuoteInfo["Forward Dividend & Yield"].split(" ")[0]
dividendYield = tickerQuoteInfo["Forward Dividend & Yield"].split(" ")[1].replace("(","").replace(")","") 
PERatio = tickerQuoteInfo["PE Ratio (TTM)"]

bookValue = tickerStats.loc[tickerStats["Attribute"]=="Book Value Per Share (mrq)"]["Value"].values[0]

shareOutstanding = tickerStats.loc[tickerStats["Attribute"]=="Shares Outstanding 5"]["Value"].values[0]
shareOutstanding = util.readableToFloat(shareOutstanding)

totalDebtOverEquity = tickerStats.loc[tickerStats["Attribute"]=="Total Debt/Equity (mrq)"]["Value"].values[0]
currentRatio = tickerStats.loc[tickerStats["Attribute"]=="Current Ratio (mrq)"]["Value"].values[0]

tickerIncomeStatement.reset_index(inplace=True)
tickerBalanceSheet.reset_index(inplace=True)

totalCurrentAssets = tickerBalanceSheet.loc[tickerBalanceSheet["Breakdown"]=="totalCurrentAssets"][datetime.datetime.strptime("2020-12-31 00:00:00", '%Y-%m-%d %H:%M:%S')].values[0]
totalCurrentLiabilities = tickerBalanceSheet.loc[tickerBalanceSheet["Breakdown"]=="totalCurrentLiabilities"][datetime.datetime.strptime("2020-12-31 00:00:00", '%Y-%m-%d %H:%M:%S')].values[0]
longTermDebt = tickerBalanceSheet.loc[tickerBalanceSheet["Breakdown"]=="longTermDebt"][datetime.datetime.strptime("2020-12-31 00:00:00", '%Y-%m-%d %H:%M:%S')].values[0]
totalLiab = tickerBalanceSheet.loc[tickerBalanceSheet["Breakdown"]=="totalLiab"][datetime.datetime.strptime("2020-12-31 00:00:00", '%Y-%m-%d %H:%M:%S')].values[0]

print (tickerQuoteInfo)
print (tickerStats)
print ("\n")
#print (tickerIncomeStatement)
#print ("\n")
print (tickerBalanceSheet)
print ("\n")

print ("currentPrice: " + str(currentPrice))
print ("marketCap: " + str(marketCap))
print ("dividendPerShare: " + str(dividendPerShare))
print ("dividendYield: " + dividendYield)
print ("bookValue: " + bookValue)
print ("shareOutstanding: " + str(shareOutstanding))
print ("totalDebtOverEquity: " + totalDebtOverEquity)
print ("PERatio: " + str(PERatio))
print ("currentRatio: " + str(currentRatio))
print ("totalCurrentAssets: " + str(totalCurrentAssets))
print ("totalCurrentLiabilities: " + str(totalCurrentLiabilities))
print ("longTermDebt: " + str(longTermDebt))
print ("totalLiab: " + str(totalLiab))
