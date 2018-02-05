#get dividend info
#dividend total
#dividend interval
#input: ALLREIT.csv
#output: PRICEREPORT.csv

#url:https://api.iextrading.com/1.0/stock/stag/dividends/1y

import csv
import requests
import json

def get_price_info(ticker):
    #return [last year sum, regular payout times, extra sum, extra times]
    #print(ticker)
    url = 'https://api.iextrading.com/1.0/stock/'+ ticker +'/quote'
    r = requests.get(url)
    if r.status_code != 200:
        return ['-2','0','0','0','0']
    data = r.json()
    #parse data
    #if paid dividend
    if len(data) == 0:
        return ['-2','0','0','0','0']
    #if paid regularly
    sum = 0.00
    return [str(data['week52High']),str(data['week52Low']),str(data['latestPrice']),str(data['peRatio']),str(data['marketCap'])]


def generate_price_report(fileName):
    newfile = open('PRICEREPORT.csv','w')
    newfile.write('Name,Ticker,Exchange,52High,52Low,latestPrice,peRatio,marketCap\n')
    with open(fileName, newline='') as csvfile:
        next(csvfile)
        csvReader = csv.reader(csvfile, delimiter=',')
        for row in csvReader:
            #requests
            data = get_price_info(row[1])
            row[0] = '\"' + row[0] + '\"'
            row = row + data
            newfile.write(",".join(row)+'\n')
    newfile.close()
if __name__ == "__main__":
    generate_price_report('ALLREIT.csv')
