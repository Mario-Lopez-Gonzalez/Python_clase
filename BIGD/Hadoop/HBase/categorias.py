import happybase
from collections import defaultdict

# Conectar a HBase
connection = happybase.Connection('ec2-44-200-191-121.compute-1.amazonaws.com', timeout=5000)  # Cambia a la dirección de tu servidor HBase
connection.open()

# Obtener la tabla
table = connection.table('tickets')

# Crear un diccionario para contar las ocurrencias de cada 'issue_category'
category_counts = defaultdict(int)

# Escanear todas las filas de la tabla
for row_key, row_data in table.scan():
    # Obtener el valor de 'issue:Issue_Category'
    issue_category = row_data.get(b'issue:Issue_Category')
    
    # Si 'issue_category' no es None, incrementar el contador para esa categoría
    if issue_category:
        category_counts[issue_category.decode('utf-8')] += 1

# Ordenar el diccionario por las cantidades de ocurrencias en orden descendente
sorted_category_counts = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)

# Mostrar los resultados ordenados
for category, count in sorted_category_counts:
    print(f"Category: {category}, Count: {count}")

# Cerrar la conexión
connection.close()
