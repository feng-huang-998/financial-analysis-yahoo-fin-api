import yahoo_fin.stock_info as si

def getQuoteInfo(ticker): 
    return si.get_quote_table(ticker)
