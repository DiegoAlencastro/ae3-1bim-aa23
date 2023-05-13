from conexion_base_datos import conn

cursor = conn.cursor()

cursor.execute("""
    select id, nombre, nacionalidad, salario, numeroCamiseta from Jugador
    """)

print('{:<2} {:<15} {:<15} {:<15} {:2}'.format('ID','Nombre', 'Nacionalidad', 'Salario','N.Camiseta'))
    
informacion = cursor.fetchall()
    
for row in informacion:
    id, nombre, nacionalidad, salario, numeroCamiseta  = row
    print('{:2d} {:<15} {:<15} {:<15} {:2d}'.format(id, nombre, nacionalidad, salario, numeroCamiseta))