from happybase import Connection

# Conectar a HBase
connection = Connection('ec2-44-200-191-121.compute-1.amazonaws.com', timeout=5000)
table = connection.table('tickets')

# Contar filas con 'Hardware' en Issue_category sin filtro en HBase
count = 0
for row in table.scan():
    # La fila es una tupla, la segunda parte (índice 1) es el diccionario con las columnas
    columns = row[1]
    # Ahora accedemos al valor de la columna 'issue:Issue_Category'
    if b'issue:Issue_Category' in columns and columns[b'issue:Issue_Category'] == b'Hardware':
        count += 1

print(f"Filas con 'Hardware' en Issue_category: {count}")


