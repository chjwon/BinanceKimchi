import ccxt
from time import time
# from usdkrw import price

start = time()

upbit = ccxt.upbit()

coinListUpbit = []
coinList = upbit.fetch_tickers()
# for i in list(coinList.keys()):
#     if i[-4:] == '/KRW':
#         temp = upbit.fetch_ohlcv(i)
#         volumeIn5 = 0
#         for j in range(5):
#             volumeIn5 += temp[-j][5]
#         if volumeIn5 > 5.787 * 5:
#             coinListUpbit.append(i)

coinListUpbit = ['1INCH/KRW', 'ADA/KRW', 'AERGO/KRW', 'AHT/KRW', 'ANKR/KRW', 'AQT/KRW', 'ARDR/KRW', 'ARK/KRW', 'ATOM/KRW', 'AXS/KRW', 'BAT/KRW', 'BCH/KRW', 'BORA/KRW', 'BSV/KRW', 'BTG/KRW', 'BTT/KRW', 'CBK/KRW', 'CHZ/KRW', 'CRE/KRW', 'CRO/KRW', 'CVC/KRW', 'DAWN/KRW', 'DKA/KRW', 'DOGE/KRW', 'DOT/KRW', 'ELF/KRW', 'ENJ/KRW', 'EOS/KRW', 'ETC/KRW', 'ETH/KRW', 'FCT2/KRW', 'FLOW/KRW', 'GAS/KRW', 'GLM/KRW', 'GRS/KRW', 'HBAR/KRW', 'HIVE/KRW', 'HUM/KRW', 'HUNT/KRW', 'ICX/KRW', 'IOST/KRW', 'IOTA/KRW', 'IQ/KRW', 'JST/KRW', 'KAVA/KRW', 'KNC/KRW', 'LINK/KRW', 'LOOM/KRW', 'LSK/KRW', 'LTC/KRW', 'MANA/KRW', 'MATIC/KRW', 'MBL/KRW', 'MED/KRW', 'META/KRW', 'MFT/KRW', 'MLK/KRW', 'MOC/KRW', 'MTL/KRW', 'MVL/KRW', 'NEO/KRW', 'NU/KRW', 'OMG/KRW', 'ONG/KRW', 'ONT/KRW', 'ORBS/KRW', 'PLA/KRW', 'POLY/KRW', 'POWR/KRW', 'PUNDIX/KRW', 'QKC/KRW', 'QTUM/KRW', 'REP/KRW', 'RFR/KRW', 'SAND/KRW', 'SBD/KRW', 'SC/KRW', 'SNT/KRW', 'SOL/KRW', 'SRM/KRW', 'SSX/KRW', 'STEEM/KRW', 'STMX/KRW', 'STORJ/KRW', 'STPT/KRW', 'STRAX/KRW', 'STRK/KRW', 'STX/KRW', 'SXP/KRW', 'TFUEL/KRW', 'THETA/KRW', 'Tokamak Network/KRW', 'TRX/KRW', 'TT/KRW', 'UPP/KRW', 'VET/KRW', 'WAVES/KRW', 'WAXP/KRW', 'XEC/KRW', 'XEM/KRW', 'XLM/KRW', 'XRP/KRW', 'XTZ/KRW', 'ZIL/KRW', 'ZRX/KRW']

coinName = 'BTC/KRW'

orderbookUpbit = upbit.fetch_order_book(coinName)
closePriceUpbit = orderbookUpbit['asks'][-1]  # present price is [0]
