from datetime import datetime
from pymongo import MongoClient
import moduleExtractYahooFinAPI as extfinapi
import moduleMongoDB as mongodb

now = datetime.now()
dt_string = now.strftime("%Y-%m-%d %H:%M:%S")

ticker = "amzn"
stockQuoteInfo = extfinapi.extractStockQuoteInfo(ticker)

stockQuoteInfoWithDateTime = {
  "symbol": ticker,
  "date": dt_string,
  "quoteInfo": stockQuoteInfo
}

print(stockQuoteInfoWithDateTime)

connection = mongodb.getConnection()
db = connection.financialDataStockDB

db.stockQuoteInfo.insert_one(stockQuoteInfoWithDateTime)
