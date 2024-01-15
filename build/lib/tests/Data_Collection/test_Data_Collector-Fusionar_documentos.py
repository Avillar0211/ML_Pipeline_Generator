from ML_Pipeline_Generator.Data_Collection.Data_Collector import DataCollector
import pandas

json = pandas.DataFrame(pandas.read_json('adventure.json'))
csv = pandas.DataFrame(pandas.read_csv('action.csv'))
xlsx = pandas.DataFrame(pandas.read_excel('crime.xlsx'))
with open('family.html', 'r', encoding="utf-8") as f:
    dfs = pandas.read_html(f.read())
    html =  pandas.DataFrame(dfs[0])

aux = ['adventure.json', 'action.csv', 'crime.xlsx', 'family.html']
c = DataCollector(aux)
res = c.readDataSources()

total = json.shape[0] + html.shape[0] + csv.shape[0] + xlsx.shape[0]

assert res.shape[0] == total, 'No ha unido bien los archivos'
