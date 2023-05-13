from conexion_base_datos import conn

conn.executescript("""
        insert into Equipo (nombre, presidente, pais)
        values ('Liga', 'Isaac Álvarez','Ecuador');
        
        insert into Equipo (nombre, presidente, pais)
        values ('Brighton', 'Tony Bloom','Inglaterra');
        
        insert into Equipo (nombre, presidente, pais)
        values ('Barcelona', 'Carlos Alfaro','Ecuador');
        """)
conn.commit();
print ("Registros ingresados")
