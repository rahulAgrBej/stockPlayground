import yfinance as yf
import pprint

abbv = yf.Ticker("ABBV")

pp = pprint.PrettyPrinter(indent=3)
pp.pprint(abbv.info)
