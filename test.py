import ccxt
from datetime import datetime

from slack import post_message, myToken
from exchanges.upbit import closePriceUpbit, coinListUpbit, start
from exchanges.binance import binance, closePriceBinance, coinListBinance, orderbookBinance
from exchanges.bithumb import closePriceBithumb, coinListBithumb
from time import time

# current channel name : #binance_ats -> need fix
channelName = '#binance_ats'
"""
binance / bithumb / upbit / 

huobi / okex / kraken / gateio / coinbase / bybit / Kucoin / ftx / poloniex
"""


print("BTC/USDT")
print("Upbit : ",   closePriceUpbit[0])
print("Binance : ", closePriceBinance[0])
print("Upbit / Binance : ",(closePriceUpbit[0]/closePriceBinance[0] - 1)*100,'%')
print("Bithumb : ", closePriceBithumb[0]) #KRW




print("==test==")
# print(coinList.keys())

# print(coinListBinance)
# print(coinListUpbit)
# print(coinListBithumb) # fix
#
# print(orderbookBinance['bids'][-1])
# print(orderbookBinance['asks'][-1])

print("time : ",time() - start)


