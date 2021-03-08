import moduleYahooFinAPI as finapi
import moduleUtil as util
import datetime
import json

#ticker = "amzn"

def extractQuoteInfo(ticker): 

    tickerQuoteInfo = finapi.getTickerQuoteTable(ticker)
    tickerStats = finapi.getTickerStats(ticker)

    print (tickerQuoteInfo)
    print (tickerStats)

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

    # Extract everytime of execution -> quote_info
    print ("currentPrice: " + str(currentPrice))
    print ("marketCap: " + str(marketCap))
    print ("dividendPerShare: " + str(dividendPerShare))
    print ("dividendYield: " + dividendYield)
    print ("bookValue: " + bookValue)
    print ("shareOutstanding: " + str(shareOutstanding))
    print ("totalDebtOverEquity: " + totalDebtOverEquity)
    print ("PERatio: " + str(PERatio))
    print ("currentRatio: " + str(currentRatio))

    quoteInfoJson = {
        "currentPrice": str(currentPrice),
        "marketCap": str(marketCap),
        "dividendPerShare": str(dividendPerShare),
        "dividendYield": str(dividendYield),
        "bookValue": str(bookValue),
        "shareOutstanding": str(shareOutstanding),
        "totalDebtOverEquity": str(totalDebtOverEquity),
        "PERatio": str(PERatio),
        "currentRatio: " + str(currentRatio)
    }

    return json.dumps(quoteInfoJson)

def extractBalanceSheetYearly(ticker): 
    tickerBalanceSheet = finapi.getBalanceSheet(ticker)
    print (tickerBalanceSheet)
    
    totalCurrentAssets = tickerBalanceSheet.loc["totalCurrentAssets"][datetime.datetime.strptime("2020-12-31 00:00:00", '%Y-%m-%d %H:%M:%S')]
    totalCurrentLiabilities = tickerBalanceSheet.loc["totalCurrentLiabilities"][datetime.datetime.strptime("2020-12-31 00:00:00", '%Y-%m-%d %H:%M:%S')]
    longTermDebt = tickerBalanceSheet.loc["longTermDebt"][datetime.datetime.strptime("2020-12-31 00:00:00", '%Y-%m-%d %H:%M:%S')]
    totalLiabilities = tickerBalanceSheet.loc["totalLiab"][datetime.datetime.strptime("2020-12-31 00:00:00", '%Y-%m-%d %H:%M:%S')]

    # Extract quarterly -> balance_sheet_yearly 
    print ("totalCurrentAssets: " + str(totalCurrentAssets))
    print ("totalCurrentLiabilities: " + str(totalCurrentLiabilities))
    print ("longTermDebt: " + str(longTermDebt))
    print ("totalLiabilities: " + str(totalLiabilities)) 

    balanceSheetYearlyJson = {
        "totalCurrentAssets": str(totalCurrentAssets),
        "totalCurrentLiabilities": str(totalCurrentLiabilities),
        "longTermDebt": str(longTermDebt),
        "totalLiabilities": str(totalLiabilities)
    }

    return json.dumps(balanceSheetYearlyJson)

def extractIncomeStatementYearly(ticker):
    tickerIncomeStatement = finapi.getIncomeStatement(ticker)
    print (tickerIncomeStatement)

    netIncomeApplicableToCommonShares = tickerIncomeStatement.loc["netIncomeApplicableToCommonShares"][datetime.datetime.strptime("2020-12-31 00:00:00", '%Y-%m-%d %H:%M:%S')]
    latest4YrNetIncomeApplicableToCommonShares = tickerIncomeStatement.loc["netIncomeApplicableToCommonShares"]

    # Extract yearly -> income_statement_yearly 
    print ("netIncomeApplicableToCommonShares: " + str(netIncomeApplicableToCommonShares))
    print ("latest4YrNetIncomeApplicableToCommonShares: " + str(latest4YrNetIncomeApplicableToCommonShares))

    incomeStatementYearlyJson = {
        print ("netIncomeApplicableToCommonShares: " + str(netIncomeApplicableToCommonShares))
        print ("latest4YrNetIncomeApplicableToCommonShares: " + str(latest4YrNetIncomeApplicableToCommonShares))
    }

    return 