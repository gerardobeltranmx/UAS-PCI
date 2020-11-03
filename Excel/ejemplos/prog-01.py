import openpyxl
#Abre archivo de excel
documento = openpyxl.load_workbook('../../datos/municipios.xlsx')
#Abre hoja de calculo
hoja = documento.get_sheet_by_name('municipios')
#Obtiene matriz de datos
matriz = hoja['A1':'A19']
#Recorre por renglones
for renglon in matriz:
    #Recorre cada celda
    for celda in renglon:
        print (celda.value)