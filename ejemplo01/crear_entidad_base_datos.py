from conexion_base_datos import conn

conn.executescript("""
        create table Equipo (
            id          integer primary key autoincrement not null,
            nombre      text,
            presidente   text,
            pais        text
        );
        """)
print ("Tabla Equipo creada")
