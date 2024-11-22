import pandas as pd

data = read_excel('./ENB2012_data.xlsx')

print(data)

rows_as_a_list = data.values.tolist()

for fila in filas_como_una_lista:
    print(fila)


###FUNCTIONS###

#Function for read excels and get the data
def read_excel(rute):
    df = pd.read_excel(rute)

    return df