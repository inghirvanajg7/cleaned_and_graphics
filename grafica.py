import pandas as pd
import matplotlib.pyplot as plt

#create a chart using the data in the DataFrame 
#read the Excel file into a DataFrame cleaned_empresa_namm.xlsx
df = pd.read_excel("cleaned_empresa_namm.xlsx")  #read the Excel file into a DataFrame

entrevistados = df['FUE A ENTREVISTA'].value_counts()

induccion = df['INDUCCIÓN'].value_counts()

sexo = df['SEXO'].value_counts()

#prom_sexo = pd.to_numeric(df['SEXO'], errors="coerce").astype(float).mean()

print(entrevistados)
print(induccion)
print(sexo)
#print(prom_sexo)


df['SEXO'].value_counts()
df['SEXO'].value_counts().plot(kind="pie", figsize=(6,6))

#build a bar chart using the data in the DataFrame 
#chart_puesto = df['INDUCCIÓN'].value_counts().plot(kind='bar')

#show the chart 
#plt.show()
#print(chart)

#build a pie chart using the data in the DataFrame 
#conteo = df['INDUCCIÓN'].value_counts()
#print(conteo)


print("Se generó el gráfico de barras para la columna 'INDUCCIÓN'")
