import yfinance as yf
import pprint

def readAristocrats(filePath):

    aristocrats = []

    f = open(filePath, 'r', encoding='utf-8-sig')
    rows = f.readlines()
    f.close()

    for row in rows:
        row = row.rstrip('\n')
        cells = row.split(',')
        aristocrats.append((cells[0], cells[1]))
    
    return aristocrats

aristocrats = readAristocrats('dividend_aristocrats.csv')
pp = pprint.PrettyPrinter(indent=3)
pp.pprint(aristocrats)


"""
abbv = yf.Ticker("ABBV")


pp.pprint(abbv.info)
"""
