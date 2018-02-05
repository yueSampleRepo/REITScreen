#get dividend info
#dividend total
#dividend interval
#input: ALLREIT.csv
#output: DIVIDENDREPORT.csv

#url:https://api.iextrading.com/1.0/stock/stag/dividends/1y

import csv
import requests
import json

def get_divident_info(ticker):
    #return [last year sum, regular payout times, extra sum, extra times]
    #print(ticker)
    url = 'https://api.iextrading.com/1.0/stock/'+ ticker +'/dividends/1y'
    r = requests.get(url)
    if r.status_code != 200:
        return ['-2','0','0','0']
    data = r.json()
    #parse data
    #if paid dividend
    if len(data) == 0:
        return ['0','0','0','0']
    #if paid regularly
    sum = 0.00
    for payout in data:
        if payout['amount'] == "":
            payout['amount'] = 0
        sum = sum + payout['amount']
    if len(data) in [2,4,12]:
        return [str(len(data)),str(sum),'0','0']
    else:
        return [str(len(data)),str(sum),str(len(data)),str(sum)]


def generate_dividend_report(fileName):
    newfile = open('DIVIDENDREPORT.csv','w')
    newfile.write('Name,Ticker,Exchange,Payout_Times,Dividend_LastYear,Irregular_Times,Irregular_Divident_LastYear\n')
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
    generate_dividend_report('ALLREIT.csv')
