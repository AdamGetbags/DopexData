# -*- coding: utf-8 -*-
"""
DOPEX API // decentralized option data
https://github.com/dopex-io/dopex-api/blob/master/docs/v1/ENDPOINTS.md
@author: adam getbags

"""

# import modules
import pandas as pd
import requests
# import time
# import plotly.express as px
# import plotly.graph_objects as go
# from plotly.offline import plot
# import numpy as np
import datetime as dt
import json

"""
GET SSOV DATA // API V2
"""

# build url for SSOVs 
url = 'https://api.dopex.io/api/v2/ssov'

# make get request
res = requests.get(url)

# convert to dataframe // the column name is the chainId
dfSSOV = pd.read_json(res.text)

# expand dictionaries to columns
dfSSOV = dfSSOV[dfSSOV.columns[0]].apply(pd.Series)

# review columns 
print(dfSSOV.columns)

# review values
for i in dfSSOV.columns:
    print(i)
    print('- ' * 9)
    print(dfSSOV[i])
    print('- ' * 9)

# review assets that SSOVs are available for
symbols = list(dfSSOV.symbol)
print(symbols)

# SSOV contract address (???)
print(dfSSOV.address)

# navigating rewards
print(dfSSOV.rewards)
print(dfSSOV.rewards[0])
print(dfSSOV.rewards[0][0])
print(dfSSOV.rewards[0][0]['amount'])
print(dfSSOV.rewards[0][0]['amount']['hex'])

# navigating epoch times
print(dfSSOV.epochTimes)
print(dfSSOV.epochTimes[0])
print(dfSSOV.epochTimes[0]['expiry'])
dtStart = dt.datetime.fromtimestamp(int(dfSSOV.epochTimes[0]['expiry']))
print(dtStart)

# # duration of vault epoch
# print(dfSSOV.duration)

# # is vault retired
# print(dfSSOV.retired)

# # SSOV contract address (???)
# print(dfSSOV.address)

# # total value locked per SSOV
# print(dfSSOV.tvl)

# # get APY metric 
# print(dfSSOV.apy)

# # underlying prices
# print(dfSSOV.underlyingPrice)

"""
GET APY DATA // API V1
"""

# assign string variables to use when creating url
assetSymbol = dfSSOV.underlyingSymbol[0]
optionType = 'CALL' # 'PUT'

# build url for APYs
url = f'https://api.dopex.io/api/v1/ssov/apy?asset={assetSymbol}'

# make get request
res = requests.get(url)

# convert response to dictionary
apyData = json.loads(res.text)

#review keys
print(apyData['apy'])

# build url for APYs with option type
url = (
    f'https://api.dopex.io/api/v1/ssov/'
    f'apy?asset={assetSymbol}&type={optionType}'
)

# make get request
res = requests.get(url)

# convert response to dictionary
apyData = json.loads(res.text)

#review keys
print(apyData['apy'])

"""
GET APY DATA // API V2
"""

# assign v2 asset symbol
assetSymbolV2 = dfSSOV.symbol[0]

# build url for APYs with option type
url = f'https://api.dopex.io/api/v2/ssov/apy?symbol={assetSymbolV2}'

# make get request
res = requests.get(url)

# convert response to dictionary
apyDataV2 = json.loads(res.text)

"""
GET DEPOSIT DATA // API V1
"""

# rdpx
assetSymbol = dfSSOV.underlyingSymbol[1]

# build url for SSOV deposits // no dice
url = (
    f'https://api.dopex.io/api/v1/ssov/'
    f'deposits?asset={assetSymbol}&type={optionType}'
)    

# make get request
res = requests.get(url)

# convert to dataframe
deposits = pd.read_json(res.text)

print(deposits)

"""
GET OPTION PRICE DATA // API V1
"""

# build url for SSOV option prices // no dice
url = (
    f'https://api.dopex.io/api/v1/ssov/'
    f'options/prices?asset={assetSymbol}&type={optionType}'
)    

# make get request
res = requests.get(url)

# convert to dataframe 
optionPrices = pd.read_json(res.text)

print(optionPrices)

"""
GET OPTION USAGE DATA // API V1
"""

# build url for SSOV option usage // no dice
url = (
    f'https://api.dopex.io/api/v1/ssov/'
    f'options/usage?asset={assetSymbol}&type={optionType}'
)    

# make get request
res = requests.get(url)

# convert to dataframe 
optionUsage = pd.read_json(res.text)

print(optionUsage)

"""
GET TOKEN PRICE DATA // API V1
"""

token = 'dpx' # 'rdpx'

# build url for current token price
url = f'https://api.dopex.io/api/v1/{token}/price'
    
# make get request
res = requests.get(url)

# convert to dataframe 
tokenPrice = json.loads(res.text)

print(tokenPrice)

"""
GET TOKEN SUPPLY DATA // API V1
"""

# build url for current token supply
url = f'https://api.dopex.io/api/v1/{token}/supply'
    
# make get request
res = requests.get(url)

# convert to dataframe 
tokenSupply = json.loads(res.text)

print(tokenSupply)

"""
GET TOKEN MARKET CAP DATA // API V1
"""

# build url for current token mkt cap
url = f'https://api.dopex.io/api/v1/{token}/market-cap'
    
# make get request
res = requests.get(url)

# convert to dataframe 
mktCap = json.loads(res.text)

print(mktCap)

"""
GET FARM TVL DATA // API V1
"""

farmName = 'dpx-weth' # 'rdpx-weth'

# build url for Farm TVL per pool
url = f'https://api.dopex.io/api/v1/farms/tvl?pool={farmName}'
    
# make get request
res = requests.get(url)

# convert to dataframe 
farmTVL = json.loads(res.text)

print(farmTVL)

"""
GET TVL DATA // API V1
"""

# build url for TVL
url = 'https://api.dopex.io/api/v1/tvl'
# url = 'https://api.dopex.io/api/v1/tvl?include=dpx-ssov,eth-ssov'
# url = (
#     f'https://api.dopex.io/api/v1/tvl?'
#     f'include=dpx-farm,rdpx-farm,dpx-weth-farm,'
#     f'rdpx-weth-farm,dpx-ssov,rdpx-ssov'
# )
    
# make get request
res = requests.get(url)

# convert to dataframe 
allTVL = json.loads(res.text)

print(allTVL)