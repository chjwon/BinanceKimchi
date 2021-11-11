import ccxt
from time import time
# from usdkrw import price

coinbase = ccxt.coinbase()
coinListCoinbase = []
coinList = coinbase.fetch_tickers()
for i in list(coinList.keys()):
    if i[-4:] == '/USD':
        temp = coinbase.fetch_ohlcv(i)
        volumeIn5 = 0
        for j in range(5):
            volumeIn5 += temp[-j][5]
        if volumeIn5 > 5.787 * 5:
            coinListCoinbase.append(i)




coinName = 'BTC/USD'
orderbookCoinbase = coinbase.fetch_ticker(coinName)
closePriceCoinbase = orderbookCoinbase['asks'][-1]  # present price is [0]


# print(orderbookCoinbase['bid'])
# print(orderbookCoinbase['ask'])
