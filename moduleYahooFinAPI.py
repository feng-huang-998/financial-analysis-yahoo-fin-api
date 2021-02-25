import yahoo_fin.stock_info as si

def getTickerQuoteTable(ticker): 
    return si.get_quote_table(ticker)

def getTickerData(ticker): 
    return si.get_data(ticker)

def getTickerStats(ticker): 
    return si.get_stats(ticker)

