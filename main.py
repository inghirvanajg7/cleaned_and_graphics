import unicodedata

import pandas as pd

#read the Excel file into a DataFrame
df = pd.read_excel("empresa_namm.xlsx")

#display the first few rows of the DataFrame
print(df.head())

#see the DataFrame's 

#display the column names of the DataFrame
print(df.columns)

#display the data types of each column in the DataFrame
print(df.dtypes)

#info() method provides a concise summary of the DataFrame, including the number of non-null values and memory usage
print(df.info()) 

print(df.isnull().sum())  #display the number of missing values in each column of the DataFrame

#fill any missing values in the FABRICA column with the string "N/A"
df['FABRICA'] = df['FABRICA'].fillna("NAMM")

#split the Fecha_Hora column into separate Fecha and Hora columns
df[['FECHA', 'HORA']] = df['FECHA Y HORA'].str.split(",", expand=True)

#the format of the Fecha column is in the format dd/mm/yyyy, so we need to specify dayfirst=True 
# when converting to datetime, without format hour, minute, second, and microsecond will be set to 0 by default  
df['FECHA_NUMERO'] = pd.to_datetime(df['FECHA'], dayfirst=True).dt.strftime('%d/%m/%Y') #convert the Fecha column to a datetime object

#df['HORA_TIME'] = pd.to_datetime(df['HORA'], format='%H:%M:%S').dt.strftime('%H:%M:%S')  #convert the Hora column to a time object

#fill any missing values in the Puesto column with the string "Ayudante General"
df['PUESTO'] = df['PUESTO'].fillna("Ayudante General")

#df['PUESTO'] = df['PUESTO'].str.capitalize()

df['FUE A ENTREVISTA'] = df['FUE A ENTREVISTA'].str.capitalize() #change capitalize the values in the Fue a Entrevista column 

df['APTO O NO APTO'] = df['APTO O NO APTO'].str.capitalize()

#change capitalize the values in the Inducción column to have the first letter capitalized
df['INDUCCIÓN'] = df['INDUCCIÓN'].str.capitalize()

#split the Nombre del Candidato column into separate Nombre and Apellido columns and put vacio if there is no Apellido, and not remove any leading or trailing whitespace from the values in the Nombre and Apellido columns
df[['NOMBRE', 'APELLIDO']] = df['NOMBRE DEL CANDIDATO'].str.split(",", expand=True).apply(lambda nombre_apellido: nombre_apellido.str.strip() if isinstance(nombre_apellido, pd.Series) else nombre_apellido)

#split the PRIMER NOMBRE and SEGUNDO NOMBRE columns into separate PRIMER NOMBRE and SEGUNDO NOMBRE columns and put vacio if there is no SEGUNDO NOMBRE, and not remove replace for N/A in the values in the PRIMER NOMBRE and SEGUNDO NOMBRE columns, and not remove any leading or trailing whitespace from the values in the PRIMER NOMBRE and SEGUNDO NOMBRE columns
df[['PRIMER NOMBRE', 'SEGUNDO NOMBRE']] = df['NOMBRE'].str.split(" ", n=1, expand=True).apply(lambda primer_segundo: primer_segundo.str.strip() if isinstance(primer_segundo, pd.Series) else primer_segundo).fillna("N/A")

#create a new column called "SEXO" that contains the gender of the employee based on the value in the "NOMBRE DEL CANDIDATO" column, if the name ends with "a" then the gender is "Femenino", otherwise it is "Masculino"
df['SEXO'] = df['PRIMER NOMBRE'].apply(lambda nombre: 'Femenino' if isinstance(nombre, str) and 
                                nombre.strip().lower().endswith("a") 
                                else 'Masculino')   # not unicodedata.normalize('NFD', nombre).encode('ascii', 'ignore').decode('utf-8').strip().lower().endswith("a") 

#count woman in the DataFrame by counting the number of rows where the Sexo column is equal to "Femenino"
#num_women = df[df['SEXO'] == "Femenino"].shape[0]
#count men in the DataFrame by counting the number of rows where the Sexo column is equal to "Masculino"
#num_men = df[df['SEXO'] == "Masculino"].shape[0]

#count the 

#-------------------clean the data by dropping any rows with missing values in the columns--------------------------------------

#fill any missing values in the columns with the string "N/A"
#df = df.fillna("N/A")  #fill any missing values in the columns with the string "N/A"

#delete columns and rows empty
df = df.dropna()  #drop any columns that are completely empty

#display the number of missing values in each column of the DataFrame
#print(df.isnull().sum())


#df['HORA'] = pd.to_datetime(df['HORA'], format='%H:%M:%S').dt.strftime('%H:%M:%S')  #change the format of the Hora column to be in the format "HH:MM:SS"

#change the format of the Hora column to be in the format "HH:MM:SS"
#df['HORA_TIME'] = pd.to_datetime(df['HORA'], format='%H:%M:%S').dt.strftime('%H:%M:%S')  

#print the cleaned DataFrame
print(df)

#saved the cleaned DataFrame to a new Excel file

df.to_excel("cleaned_empresa_namm.xlsx", index=False) #save the cleaned DataFrame to a new Excel file
print("Se guardó el archivo 'cleaned_empresa_namm.xlsx'")

#change the format of the Hora column to be in the format "HH:MM:SS"
#df['HORA'] = pd.to_datetime(df['HORA'], format='%H:%M:%S').dt.strftime('%H:%M:%S')  


#display the summary statistics of the DataFrame
#print(df.describe())

#display the number of missing values in each column of the DataFrame
#print(df.isnull().sum())

#display the unique values in each column of the DataFrame
#for column in df.columns:
#    print(f"Unique values in column '{column}': {df[column].unique()}")

#drop any duplicate rows in the DataFrame
#df = df.drop_duplicates()

#display the number of rows and columns in the DataFrame after dropping duplicates
#print(df.shape)

#clean the data by dropping any rows with missing values
#df_cleaned = df.dropna()

#display the number of rows and columns in the cleaned DataFrame
#print(df_cleaned.shape)

#split hora and fecha into separate columns
#df_cleaned[['Fecha', 'Hora']] = df_cleaned['Fecha_Hora'].str.split(",", expand=True)

#display the first few rows of the cleaned DataFrame with separate Fecha and Hora columns
#print(df_cleaned.head())

#display format of the Fecha column
#print(df_cleaned['Fecha'].head())