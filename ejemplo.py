import  sqlite3

conexion=sqlite3.connect("ejemplo.db")
cursor=conexion.cursor()

#cursor.execute('''CREATE TABLE usuarios(id INTEGER PRIMARY KEY,usuario TEXT, contrasena TEXT,rol TEXT)''')

#cursor.execute("INSERT INTO usuarios (usuario, contrasena, rol) VALUES (?, ?, ?)", ("admin", "admin","administrador"))
#cursor.execute("DELETE FROM usuarios")
#cursor.execute("DROP TABLE usuarios")

#conexion.commit()
cursor.execute("SELECT * from usuarios")

resultado=cursor.fetchone()


if resultado is not None:
    nombre_de_usuario = resultado[1]
    contrasena=resultado[2]
    rol_de_usuario=resultado[3]
    print(f"El nombre de usuario es: {nombre_de_usuario} ,contraseña :{contrasena}y el rol: {rol_de_usuario}")
else:
    print("No se encontró ningún nombre de usuario.")

conexion.close()
