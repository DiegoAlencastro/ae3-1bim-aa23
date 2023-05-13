from conexion_base_datos import conn

conn.executescript("""
        create table Jugador (
            id              integer primary key autoincrement not null,
            nombre          text,
            nacionalidad    text,
            salario         integer,
            numeroCamiseta  integer
        );
        """)
print ("Tabla Jugador creada")
