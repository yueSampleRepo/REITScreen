# REITScreen
Screen single stocks and ETFs traded on NYSE and NASDAQ, including both equity and mortgage types

## Aspects Considered
The screen compares:
- absolute annual divident yield
- yield percentage ( to price)
- yield percentage average
- market momentuem
- index comparison (capital gain)
- peer comparison (capital gain)
- FR performance

## data source 
- stock list
* http://topforeignstocks.com/stock-lists/the-complete-list-of-reit-stocks-trading-on-the-nyse/
* http://topforeignstocks.com/stock-lists/the-complete-list-of-reits-stocks-trading-on-nasdaq/
- current annual dividend
*iextrading.com
- divident growth trend
*iextrading.com
- news
*intrinio

## screen creteria
- high annual yield dividend
- steady dividend growth
- solid FR performance
- below market pricing
* price/divident cent compare to market average
* growth rate compare to market average

## raw output
name,ticker,exchange, dividend/last year,payout interval,surprise payout, surprise amount sum,price BOY, price EOY,capital gain/last year,average price/sum dividend,current price/sum dividend


