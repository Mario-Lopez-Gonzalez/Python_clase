import happybase
from collections import Counter

# Conectar a HBase
connection = happybase.Connection('ec2-44-200-191-121.compute-1.amazonaws.com', timeout=5000)  # Cambia la dirección si es necesario
connection.open()

# Obtener la tabla
table = connection.table('tickets')

# Crear un contador para las respuestas técnicas
tech_response_counts = Counter()

# Escanear todas las filas de la tabla
for row_key, row_data in table.scan():
    # Obtener el valor de 'tech_response' de la fila
    tech_response = row_data.get(b'issue:Tech_Response')
    
    # Si hay un valor para 'tech_response', incrementamos su contador
    if tech_response:
        tech_response = tech_response.decode('utf-8')
        tech_response_counts[tech_response] += 1

# Ordenar los resultados por la cantidad (de mayor a menor) y tomar los 3 primeros
top_3_responses = tech_response_counts.most_common(3)

# Mostrar los resultados
for tech_response, count in top_3_responses:
    print(f"Tech Response: {tech_response}, Count: {count}")

# Cerrar la conexión
connection.close()
