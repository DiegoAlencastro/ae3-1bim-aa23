from conexion_base_datos import conn

conn.executescript("""
        insert into Jugador (nombre, nacionalidad, salario, numeroCamiseta)
        values ('Diego', 'Ecuatoriana',1500,12);
        
        insert into Jugador (nombre, nacionalidad, salario, numeroCamiseta)
        values ('Moises', 'Ecuatoriana',8000,18);
        
        insert into Jugador (nombre, nacionalidad, salario, numeroCamiseta)
        values ('Pervis', 'Ecuatoriana',10000,16);
        """)
conn.commit();
print ("Registros ingresados")
