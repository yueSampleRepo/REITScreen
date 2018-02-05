#get dividend info
#dividend total
#dividend interval
#input: ALLREIT.csv
#output: PRICEREPORT.csv

#url:https://api.iextrading.com/1.0/stock/stag/dividends/1y

import csv
import requests
import json

def get_divident_info(ticker):
    #return [last year sum, regular payout times, extra sum, extra times]
    #print(ticker)
    url = 'https://api.iextrading.com/1.0/stock/'+ ticker +'/financials'
    r = requests.get(url)
    if r.status_code != 200:
        return ['-2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']
    data = r.json()['financials']
    #parse data
    #if paid dividend
    if len(data) == 0:
        return ['-2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']
    #if paid regularly
    return ['0',str(data[0]['operatingIncome']),str(data[1]['operatingIncome']),str(data[2]['operatingIncome']),str(data[3]['operatingIncome'])
        ,str(data[0]['totalAssets']),str(data[1]['totalAssets']),str(data[2]['totalAssets']),str(data[3]['totalAssets'])
        ,str(data[0]['shareholderEquity']),str(data[1]['shareholderEquity']),str(data[2]['shareholderEquity']),str(data[3]['shareholderEquity'])
        ,str(data[0]['totalRevenue']),str(data[1]['totalRevenue']),str(data[2]['totalRevenue']),str(data[3]['totalRevenue'])]


def generate_price_report(fileName):
    newfile = open('FINREPORT.csv','w')
    newfile.write('Name,Ticker,Exchange,200,Q1Income,Q2Income,Q3Income,Q4Income,Q1TA,Q2TA,Q3TA,Q4TA,Q1E,Q2E,Q3E,Q4E,Q1R,Q2R,Q3R,Q4R\n')
    with open(fileName, newline='') as csvfile:
        next(csvfile)
        csvReader = csv.reader(csvfile, delimiter=',')
        for row in csvReader:
            #requests
            data = get_divident_info(row[1])
            row[0] = '\"' + row[0] + '\"'
            row = row + data
            newfile.write(",".join(row)+'\n')
    newfile.close()
if __name__ == "__main__":
    generate_price_report('ALLREIT.csv')
