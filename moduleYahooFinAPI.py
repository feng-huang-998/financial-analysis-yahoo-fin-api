import yahoo_fin.stock_info as si

def getTickerQuoteTable(ticker): 
  return si.get_quote_table(ticker)

def getTickerData(ticker): 
  return si.get_data(ticker)

def getTickerStats(ticker): 
  ticketStats = si.get_stats(ticker)
  return ticketStats

def getIncomeStatement(ticker): 
  return si.get_income_statement(ticker)

def getBalanceSheet(ticker): 
  return si.get_balance_sheet(ticker)

def getCashFlow(ticker): 
  return si.get_cash_flow(ticker)

def getDowJonesList(): 
  return si.tickers_dow()

def getSP500List():
  return si.tickers_sp500()

def getNasdaqList():
  return si.tickers_nasdaq()
