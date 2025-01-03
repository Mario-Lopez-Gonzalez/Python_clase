import csv
import happybase

# Conectar a HBase
connection = happybase.Connection('ec2-44-200-191-121.compute-1.amazonaws.com', timeout=5000)
print(connection.tables())
table = connection.table('tickets')

# Leer el CSV y cargar los datos
with open('/home/iabd/Documentos/Python_clase/BIGD/Hadoop/HBase/datos/tech_support_dataset.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        row_key = row['Conversation_ID']  # Usa una columna como clave de fila
        table.put(row_key, {
            'customer:Conversation_ID': row['Conversation_ID'],
            'issue:Customer_Issue': row['Customer_Issue'],
            'issue:Issue_Category': row['Issue_Category'],
            'issue:Issue_Status': row['Issue_Status'],
            'issue:Resolution_Time': row['Resolution_Time'],
            'issue:Tech_Response': row['Tech_Response']
        })

print("Datos cargados en HBase")