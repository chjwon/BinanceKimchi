import ccxt
from datetime import datetime
from slack import post_message, myToken

binance = ccxt.binance()


# coinList with /USDT
coinListBinance = []
# coinList = binance.fetch_tickers()
# for i in list(coinList.keys()):
#     if i[-5:] == '/USDT':
#         temp = binance.fetch_ohlcv(i)
#         volumeIn5 = 0
#         for j in range(5):
#             volumeIn5 += temp[-j][5]
#         if volumeIn5 > 5.787 * 5:
#             coinListBinance.append(i)
coinListBinance = ['BTC/USDT', 'ETH/USDT', 'BNB/USDT', 'BCC/USDT', 'NEO/USDT', 'LTC/USDT', 'QTUM/USDT', 'ADA/USDT', 'XRP/USDT', 'EOS/USDT', 'TUSD/USDT', 'IOTA/USDT', 'XLM/USDT', 'ONT/USDT', 'TRX/USDT', 'ETC/USDT', 'ICX/USDT', 'NULS/USDT', 'VET/USDT', 'PAX/USDT', 'BCH/USDT', 'BSV/USDT', 'USDC/USDT', 'LINK/USDT', 'WAVES/USDT', 'BTT/USDT', 'ONG/USDT', 'HOT/USDT', 'ZIL/USDT', 'ZRX/USDT', 'FET/USDT', 'BAT/USDT', 'XMR/USDT', 'ZEC/USDT', 'IOST/USDT', 'CELR/USDT', 'DASH/USDT', 'NANO/USDT', 'OMG/USDT', 'THETA/USDT', 'ENJ/USDT', 'MITH/USDT', 'MATIC/USDT', 'ATOM/USDT', 'TFUEL/USDT', 'ONE/USDT', 'FTM/USDT', 'ALGO/USDT', 'GTO/USDT', 'ERD/USDT', 'DOGE/USDT', 'DUSK/USDT', 'ANKR/USDT', 'WIN/USDT', 'COS/USDT', 'NPXS/USDT', 'COCOS/USDT', 'MTL/USDT', 'TOMO/USDT', 'PERL/USDT', 'DENT/USDT', 'MFT/USDT', 'KEY/USDT', 'STORM/USDT', 'DOCK/USDT', 'WAN/USDT', 'FUN/USDT', 'CVC/USDT', 'CHZ/USDT', 'BAND/USDT', 'BUSD/USDT', 'BEAM/USDT', 'XTZ/USDT', 'REN/USDT', 'RVN/USDT', 'HC/USDT', 'HBAR/USDT', 'NKN/USDT', 'STX/USDT', 'KAVA/USDT', 'ARPA/USDT', 'IOTX/USDT', 'RLC/USDT', 'CTXC/USDT', 'TROY/USDT', 'VITE/USDT', 'FTT/USDT', 'EUR/USDT', 'OGN/USDT', 'DREP/USDT', 'BULL/USDT', 'BEAR/USDT', 'ETHBULL/USDT', 'ETHBEAR/USDT', 'TCT/USDT', 'WRX/USDT', 'BTS/USDT', 'LSK/USDT', 'BNT/USDT', 'LTO/USDT', 'EOSBULL/USDT', 'EOSBEAR/USDT', 'XRPBULL/USDT', 'STRAT/USDT', 'AION/USDT', 'MBL/USDT', 'COTI/USDT', 'BNBBULL/USDT', 'BNBBEAR/USDT', 'STPT/USDT', 'WTC/USDT', 'DATA/USDT', 'XZC/USDT', 'SOL/USDT', 'CTSI/USDT', 'HIVE/USDT', 'CHR/USDT', 'BTCUP/USDT', 'BTCDOWN/USDT', 'GXS/USDT', 'ARDR/USDT', 'LEND/USDT', 'MDT/USDT', 'STMX/USDT', 'KNC/USDT', 'REP/USDT', 'LRC/USDT', 'PNT/USDT', 'COMP/USDT', 'SC/USDT', 'ZEN/USDT', 'SNX/USDT', 'ETHUP/USDT', 'ETHDOWN/USDT', 'ADADOWN/USDT', 'LINKUP/USDT', 'LINKDOWN/USDT', 'VTHO/USDT', 'DGB/USDT', 'GBP/USDT', 'SXP/USDT', 'MKR/USDT', 'DAI/USDT', 'STORJ/USDT', 'BNBUP/USDT', 'BNBDOWN/USDT', 'XTZUP/USDT', 'XTZDOWN/USDT', 'MANA/USDT', 'AUD/USDT', 'BAL/USDT', 'BLZ/USDT', 'IRIS/USDT', 'KMD/USDT', 'JST/USDT', 'SRM/USDT', 'ANT/USDT', 'CRV/USDT', 'SAND/USDT', 'OCEAN/USDT', 'DOT/USDT', 'LUNA/USDT', 'RSR/USDT', 'BZRX/USDT', 'SUSHI/USDT', 'KSM/USDT', 'EGLD/USDT', 'DIA/USDT', 'RUNE/USDT', 'FIO/USDT', 'UMA/USDT', 'EOSUP/USDT', 'EOSDOWN/USDT', 'TRXUP/USDT', 'TRXDOWN/USDT', 'XRPUP/USDT', 'XRPDOWN/USDT', 'DOTUP/USDT', 'DOTDOWN/USDT', 'BEL/USDT', 'WING/USDT', 'LTCUP/USDT', 'LTCDOWN/USDT', 'UNI/USDT', 'NBS/USDT', 'OXT/USDT', 'SUN/USDT', 'AVAX/USDT', 'HNT/USDT', 'FLM/USDT', 'UNIUP/USDT', 'UNIDOWN/USDT', 'ORN/USDT', 'UTK/USDT', 'XVS/USDT', 'ALPHA/USDT', 'AAVE/USDT', 'NEAR/USDT', 'SXPUP/USDT', 'SXPDOWN/USDT', 'FIL/USDT', 'FILUP/USDT', 'FILDOWN/USDT', 'YFIUP/USDT', 'YFIDOWN/USDT', 'INJ/USDT', 'AUDIO/USDT', 'CTK/USDT', 'AKRO/USDT', 'AXS/USDT', 'HARD/USDT', 'DNT/USDT', 'STRAX/USDT', 'UNFI/USDT', 'ROSE/USDT', 'AVA/USDT', 'XEM/USDT', 'AAVEUP/USDT', 'AAVEDOWN/USDT', 'SKL/USDT', 'SUSHIUP/USDT', 'SUSHIDOWN/USDT', 'XLMUP/USDT', 'XLMDOWN/USDT', 'GRT/USDT', 'JUV/USDT', 'PSG/USDT', '1INCH/USDT', 'REEF/USDT', 'OG/USDT', 'ATM/USDT', 'ASR/USDT', 'CELO/USDT', 'RIF/USDT', 'BTCST/USDT', 'TRU/USDT', 'CKB/USDT', 'TWT/USDT', 'FIRO/USDT', 'LIT/USDT', 'SFP/USDT', 'DODO/USDT', 'CAKE/USDT', 'ACM/USDT', 'BADGER/USDT', 'FIS/USDT', 'OM/USDT', 'POND/USDT', 'DEGO/USDT', 'ALICE/USDT', 'LINA/USDT', 'PERP/USDT', 'RAMP/USDT', 'SUPER/USDT', 'CFX/USDT', 'EPS/USDT', 'AUTO/USDT', 'TKO/USDT', 'PUNDIX/USDT', 'TLM/USDT', '1INCHUP/USDT', '1INCHDOWN/USDT', 'MIR/USDT', 'BAR/USDT', 'FORTH/USDT', 'BAKE/USDT', 'BURGER/USDT', 'SLP/USDT', 'SHIB/USDT', 'ICP/USDT', 'AR/USDT', 'POLS/USDT', 'MDX/USDT', 'MASK/USDT', 'LPT/USDT', 'NU/USDT', 'XVG/USDT', 'ATA/USDT', 'GTC/USDT', 'TORN/USDT', 'KEEP/USDT', 'ERN/USDT', 'KLAY/USDT', 'PHA/USDT', 'MLN/USDT', 'DEXE/USDT', 'C98/USDT', 'CLV/USDT', 'QNT/USDT', 'FLOW/USDT', 'TVK/USDT', 'MINA/USDT', 'RAY/USDT', 'ALPACA/USDT', 'MBOX/USDT', 'FOR/USDT', 'REQ/USDT', 'GHST/USDT', 'WAXP/USDT', 'TRIBE/USDT', 'XEC/USDT', 'ELF/USDT', 'DYDX/USDT', 'POLY/USDT', 'IDEX/USDT', 'VIDT/USDT', 'USDP/USDT', 'GALA/USDT', 'ILV/USDT', 'YGG/USDT', 'SYS/USDT', 'DF/USDT', 'FRONT/USDT', 'CVP/USDT', 'AGLD/USDT', 'RAD/USDT', 'BETA/USDT', 'RARE/USDT', 'LAZIO/USDT', 'CHESS/USDT', 'ADX/USDT', 'AUCTION/USDT']


coinName = 'BTC/USDT' # temp
# Get coin list and filter coin by volatilty
# 86400 sec per day volume have to be 500000dollar per day == 5.787 dollar per sec

orderbookBinance = binance.fetch_order_book(coinName)
closePriceBinance = orderbookBinance['asks'][-1]  # present price is [0]


# ohlcvsBinacne = binance.fetch_ohlcv(coinName)

# for ohlc in ohlcvsBinacne:
#     print(datetime.fromtimestamp(ohlc[0]/1000).strftime('%Y-%m-%d %H:%M:%S'))


# present = ohlcvsBinacne[-1]
# print(present)

# messageBinance = "Time : " + str(datetime.fromtimestamp(present[0] / 1000).strftime('%Y-%m-%d %H:%M:%S')) + \
#                  "\n" + "open : " + str(present[1]) + \
#                  "\n" + "high : " + str(present[2]) + \
#                  "\n" + "low : " + str(present[3]) + \
#                  "\n" + "close : " + str(present[4]) +\
#                  "\n" + "volume : " + str(present[5])

# tempMessage = "[Binance ex] : price : " + str(closePriceBinance[0]) + \
#               " amount : " + str(closePriceBinance[1]) + \
#               " current : " + str(present[4])

# post_message(myToken,'#autotrading',tempMessage)
