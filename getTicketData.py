from yahoo_fin.stock_info import get_data

amazon_daily = {} 
amazon_daily["amzn"] = get_data("amzn")
print (amazon_daily)

