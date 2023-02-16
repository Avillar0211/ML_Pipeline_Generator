import sys
import pandas

def main():
    print("json")
    dfjson = pandas.read_json(sys.argv[0] + '.json')
    with open('salidajsonOK.csv', 'w') as output_file:
        output_file.write(dfjson.to_csv())

main()
    