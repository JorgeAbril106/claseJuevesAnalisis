import pandas as pd

#Crear un DataFrame22222

data = {
     "Nombre": ["Ana","Luis",None,"Luis"],
     "Edad": [23,34,None,34],
     "Ciudad": ["Bogota","Medellin",None,"Medellin"]
    }

print(data)
#En este segmento por medio de la clase Dataframe llamandola con pandas (pd) convertimos nuestro conjunto de datos
dataConvertidaADataFrame = pd.DataFrame(data)
print(dataConvertidaADataFrame)
print("DATAFRAME CON LOS \nDATOS NULOS ELIMINADOS")
dataSinNulos = dataConvertidaADataFrame.dropna()

print(dataSinNulos)

print(dataSinNulos.duplicated())
dataSinDuplicados = dataSinNulos.drop_duplicates()
print(dataSinDuplicados)
promedioEdades = dataSinDuplicados["Edad"].mean()
medianaEdades = dataSinDuplicados["Edad"].median()
desviacionEstandarEdades = dataSinDuplicados["Edad"].std()
print("=====Promedio Edad=====")
print(promedioEdades)
print("=====Mediana Edad=====")
print(medianaEdades)
print("=====Desviacion Estandar de la Edad=====")
print(desviacionEstandarEdades)

print(dataSinDuplicados["Edad"].min())
print(dataSinDuplicados["Edad"].max())

filtroMayores = dataSinDuplicados[dataSinDuplicados["Edad"]>30]
print(filtroMayores)

#print(dataConvertidaADataFrame["Nombre"])

#print(dataConvertidaADataFrame)


#edades = []

#edades = dataConvertidaADataFrame["Edad"]

#print("Estas son las personas registradas que pueden votar")

#for edad in edades:
#    if edad > 18:
#        print(f'Las edades de las personas que pueden votar {edad}')

#Esta funcion me permite acceder a los datos del dataframe por medio de la posicion
#print(dataConvertidaADataFrame.iloc[0])

#Esta funcion me permite acceder a los datos por columnas 
#print(dataConvertidaADataFrame.loc[:,["Nombre","Ciudad"]])

#print("Filtro personas mayores de edad: ")

#filtroMayores = dataConvertidaADataFrame[dataConvertidaADataFrame["Edad"]>18]

#print(filtroMayores)

#filtroPersonasNotBogota = dataConvertidaADataFrame[dataConvertidaADataFrame["Ciudad"]!="Bogota"]

#print(filtroPersonasNotBogota)



#dataConvertidaADataFrame['EdadesConIva'] = dataConvertidaADataFrame["Edad"] * 0.19
#print(dataConvertidaADataFrame)
#print(dataConvertidaADataFrame.isnull())
#print("Cantidad de valores nulos: ")
#print(dataConvertidaADataFrame.isnull().sum())

#dataConvertidaADataFrame['Ciudad'] = dataConvertidaADataFrame['Ciudad'].fillna("Sogamoso")


#dataConvertidaADataFrame['Edad'] = dataConvertidaADataFrame['Edad'].fillna(dataConvertidaADataFrame['Edad'].mean())
#print(dataConvertidaADataFrame)




#dataConvertidaADataFrame = dataConvertidaADataFrame.drop(columns="Ciudad")

#dataConvertidaADataFrame = dataConvertidaADataFrame.rename(columns= {'EdadesConIva':'EdadesModificadas'})

#print(dataConvertidaADataFrame)

#este es ele ejemplo de la clase