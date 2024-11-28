import happybase
from collections import defaultdict

# Conectar a HBase
connection = happybase.Connection('ec2-44-200-191-121.compute-1.amazonaws.com', timeout=5000)  # Cambia la dirección si es necesario
connection.open()

# Obtener la tabla
table = connection.table('tickets')

# Diccionarios para contar las respuestas y las resueltas
tech_response_counts = defaultdict(int)
resolved_counts = defaultdict(int)

# Escanear todas las filas de la tabla
for row_key, row_data in table.scan():
    # Obtener los valores de 'tech_response' y 'issue_status'
    tech_response = row_data.get(b'issue:Tech_Response')
    issue_status = row_data.get(b'issue:Issue_Status')
    
    if tech_response:
        tech_response = tech_response.decode('utf-8')
        tech_response_counts[tech_response] += 1
        
        # Si el estado de la incidencia es resuelto, contar como resuelto
        if issue_status:
            issue_status = issue_status.decode('utf-8')
            if issue_status == 'Resolved' or issue_status == 'Resolved after follow-up':
                resolved_counts[tech_response] += 1

# Calcular el ratio de resolución y ordenar por el ratio
tech_response_ratios = []

for tech_response in tech_response_counts:
    total_count = tech_response_counts[tech_response]
    resolved_count = resolved_counts.get(tech_response, 0)
    
    # Calcular el ratio de resolución
    if total_count > 0:
        resolution_ratio = (resolved_count * 100.0) / total_count
    else:
        resolution_ratio = 0.0
    
    tech_response_ratios.append((tech_response, total_count, resolution_ratio))

# Ordenar los resultados por ratio de resolución (de mayor a menor)
sorted_tech_responses = sorted(tech_response_ratios, key=lambda x: x[2], reverse=True)

# Mostrar los resultados
for tech_response, count, resolution_ratio in sorted_tech_responses:
    print(f"Tech Response: {tech_response}, Response Count: {count}, Resolution Ratio: {resolution_ratio:.2f}%")

# Cerrar la conexión
connection.close()
