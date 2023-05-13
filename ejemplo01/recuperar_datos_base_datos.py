from conexion_base_datos import conn

cursor = conn.cursor()

cursor.execute("""
    select id, nombre, presidente, pais from Equipo
    """)

print('{:<2} {:<15} {:<15} {:<15}'.format('ID','Nombre', 'Presidente', 'Pais'))
    
informacion = cursor.fetchall()
    
for row in informacion:
    id, nombre, presidente, pais = row
    print('{:2d} {:<15} {:<15} {:<15}'.format(id, nombre, presidente, pais))