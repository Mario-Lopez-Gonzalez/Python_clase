import happybase

# Conectar a HBase
connection = happybase.Connection('ec2-44-200-191-121.compute-1.amazonaws.com', timeout=5000)  # Cambia la dirección si es necesario
connection.open()

# Obtener la tabla
table = connection.table('tickets')

# Inicializar los contadores
resolved_count = 0
total_count = 0

# Escanear todas las filas de la tabla
for row_key, row_data in table.scan():
    # Obtener el valor de 'issue_status' de la fila
    issue_status = row_data.get(b'issue:Issue_Status')
    
    # Asegurarnos de que issue_status no sea None
    if issue_status:
        issue_status = issue_status.decode('utf-8')
        total_count += 1
        
        # Contar las filas que tienen 'Resolved' o 'Resolved after follow-up' como status
        if issue_status == 'Resolved' or issue_status == 'Resolved after follow-up':
            resolved_count += 1

# Calcular el porcentaje de incidencias resueltas
if total_count > 0:
    resolved_percentage = (resolved_count * 100.0) / total_count
    print(f"Porcentaje de incidencias resueltas: {resolved_percentage:.2f}%")
else:
    print("No hay filas en la tabla.")

# Cerrar la conexión
connection.close()
