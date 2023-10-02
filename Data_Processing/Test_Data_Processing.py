import Data_Processor
from Data_Processor import DataProcessor
import pandas

array = ['Eliminar_duplicados', 'Valor_medio_en_nulos', 'Eliminar_outliers']
aux = pandas.read_csv('contaminación_cortado.csv')
df = pandas.DataFrame(aux)
c = DataProcessor(df, array)
res = c.data_processing()
with open('salidafusion.csv', 'w', encoding="utf-8") as output_file:
    output_file.write(res.to_csv())

print('ok')

