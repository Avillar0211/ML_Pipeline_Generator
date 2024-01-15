from ML_Pipeline_Generator.Data_Collection.Data_Collector import DataCollector

aux = ['adventure.json', 'action.csv', 'crime.xlsx', 'family.html']
c = DataCollector(aux)
res = c.readDataSources()
with open('salidafusion.csv', 'w', encoding="utf-8") as output_file:
    output_file.write(res.to_csv())

print('ok')

