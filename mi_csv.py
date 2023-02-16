import sys
import pandas

def main():
    print("csv")
    dfcsv = pandas.read_csv(sys.argv[0] + '.csv')
    with open('salidacsvOK.csv', 'w') as output_file:
        output_file.write(dfcsv.to_csv())

main()
    