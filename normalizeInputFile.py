#normalize csv input
#readin
#trim name and Ticker
#exam if name null
#exam if ticker null
#combine lists to new file
#output ALLREIT.csv
#new file coolumn
#Name,Ticker,Exchange
import csv

def nomalize_input_file(fileName,exchangeName,fullFileName):
    with open(fileName, newline='') as csvfile:
        next(csvfile)
        csvReader = csv.reader(csvfile, delimiter=',')
        invalidRow = []
        for row in csvReader:
            if row[1].strip() == '' or row[2].strip() == '':
                print(row[0])
                invalidRow.append(row[0])
        csvfile.seek(0)
        next(csvfile)
        newfile = open(fullFileName, 'a')
        if invalidRow == []:
            for row in csvReader:
                newfile.write('\"' + row[1].strip() + '\",' + row[2].strip() + ',' + exchangeName +'\n')
        else:
            print("fix the input")
        newfile.close()

def import_file():
    nyseFile = "NYSE.csv"
    nasFile = "NASDAQ.csv"

    fullFile = "ALLREIT.csv"
    with open(fullFile, 'w') as newfile:
        newfile.write('Name,Ticker,Exchange\n')
    print("normalize NYSE file...")
    nomalize_input_file(nyseFile,'NYSE',fullFile)
    print("normalize NASDAQ file...")
    nomalize_input_file(nasFile,'NASDAQ',fullFile)

if __name__ == "__main__":
    import_file()
