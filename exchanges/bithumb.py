import ccxt

bithumb = ccxt.bithumb()

coinListBithumb = []
coinList = bithumb.fetch_tickers()
# for i in list(coinList.keys()):
#     if i[-4:] == '/KRW':
#         temp = bithumb.fetch_ohlcv(i)
#         volumeIn5 = 0
#         for j in range(5):
#             volumeIn5 += temp[-j][5]
#         if volumeIn5 > 5.787 * 5:
#             coinListBithumb.append(i)
coinListBithumb = ['BTC/KRW', 'ETH/KRW', 'LTC/KRW', 'ETC/KRW', 'XRP/KRW', 'BCH/KRW', 'QTUM/KRW', 'BTG/KRW', 'EOS/KRW', 'ICX/KRW', 'TRX/KRW', 'ELF/KRW', 'OMG/KRW', 'KNC/KRW', 'GLM/KRW', 'ZIL/KRW', 'WAXP/KRW', 'POWR/KRW', 'LRC/KRW', 'STEEM/KRW', 'STRAX/KRW', 'ZRX/KRW', 'REP/KRW', 'XEM/KRW', 'SNT/KRW', 'ADA/KRW', 'CTXC/KRW', 'BAT/KRW', 'WTC/KRW', 'THETA/KRW', 'LOOM/KRW', 'WAVES/KRW', 'TRUE/KRW', 'LINK/KRW', 'ENJ/KRW', 'VET/KRW', 'MTL/KRW', 'IOST/KRW', 'TMTG/KRW', 'QKC/KRW', 'HDAC/KRW', 'AMO/KRW', 'BSV/KRW', 'ORBS/KRW', 'TFUEL/KRW', 'VALOR/KRW', 'CON/KRW', 'ANKR/KRW', 'MIX/KRW', 'CRO/KRW', 'FX/KRW', 'CHR/KRW', 'MBL/KRW', 'MXC/KRW', 'FCT/KRW', 'TRV/KRW', 'DAD/KRW', 'WOM/KRW', 'SOC/KRW', 'EM/KRW', 'BOA/KRW', 'FLETA/KRW', 'SXP/KRW', 'COS/KRW', 'APIX/KRW', 'EL/KRW', 'BASIC/KRW', 'HIVE/KRW', 'XPR/KRW', 'VRA/KRW', 'FIT/KRW', 'EGG/KRW', 'BORA/KRW', 'ARPA/KRW', 'APM/KRW', 'CKB/KRW', 'AERGO/KRW', 'ANW/KRW', 'CENNZ/KRW', 'EVZ/KRW', 'CYCLUB/KRW', 'SRM/KRW', 'QTCON/KRW', 'UNI/KRW', 'YFI/KRW', 'UMA/KRW', 'AAVE/KRW', 'COMP/KRW', 'REN/KRW', 'BAL/KRW', 'RSR/KRW', 'NMR/KRW', 'RLC/KRW', 'UOS/KRW', 'SAND/KRW', 'GOM2/KRW', 'RINGX/KRW', 'BEL/KRW', 'OBSR/KRW', 'ORC/KRW', 'POLA/KRW', 'AWO/KRW', 'ADP/KRW', 'DVI/KRW', 'GHX/KRW', 'MIR/KRW', 'MVC/KRW', 'BLY/KRW', 'WOZX/KRW', 'ANV/KRW', 'GRT/KRW', 'MM/KRW', 'BIOT/KRW', 'XNO/KRW', 'SNX/KRW', 'RAI/KRW', 'COLA/KRW', 'NU/KRW', 'OXT/KRW', 'LINA/KRW', 'MAP/KRW', 'AQT/KRW', 'WIKEN/KRW', 'CTSI/KRW', 'MANA/KRW', 'LPT/KRW', 'MKR/KRW', 'SUSHI/KRW', 'ASM/KRW', 'PUNDIX/KRW', 'CELR/KRW', 'LF/KRW', 'ARW/KRW', 'MSB/KRW', 'RLY/KRW', 'OCEAN/KRW', 'BFC/KRW', 'ALICE/KRW', 'CAKE/KRW', 'BNT/KRW', 'XVS/KRW', 'CHZ/KRW', 'AXS/KRW', 'DAI/KRW', 'MATIC/KRW', 'BAKE/KRW', 'VELO/KRW', 'BCD/KRW', 'XLM/KRW', 'GXC/KRW', 'BTT/KRW', 'VSYS/KRW', 'IPX/KRW', 'WICC/KRW', 'ONT/KRW', 'LUNA/KRW', 'AION/KRW', 'META/KRW', 'KLAY/KRW', 'ONG/KRW', 'ALGO/KRW', 'JST/KRW', 'XTZ/KRW', 'MLK/KRW', 'WEMIX/KRW', 'DOT/KRW', 'ATOM/KRW', 'SSX/KRW', 'TEMCO/KRW', 'HIBS/KRW', 'BURGER/KRW', 'DOGE/KRW', 'KSM/KRW', 'CTK/KRW', 'XYM/KRW', 'BNB/KRW', 'SUN/KRW', 'XEC/KRW', 'PCI/KRW', 'SOL/KRW']



coinName = 'BTC/KRW'

orderbookBithumb = bithumb.fetch_order_book(coinName)
closePriceBithumb = orderbookBithumb['asks'][-1]  # present price is [0]