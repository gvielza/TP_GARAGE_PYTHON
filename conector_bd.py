import sqlite3
conexion = sqlite3.connect('mi_base_de_datos.db')
cursor = conexion.cursor()

#cursor.execute('''CREATE TABLE usuarios
#(id INTEGER PRIMARY KEY, usuario TEXT, contrasena TEXT)''')
cursor.execute("INSERT INTO usuarios (usuario, contrasena) VALUES (?, ?)", ("admin", "admin"))
conexion.commit()

#cursor.execute("SELECT * FROM usuarios")
#cursor.execute("DELETE  FROM usuarios")
#conexion.commit()

resultado = cursor.fetchone()

if resultado is not None:
    nombre_de_usuario = resultado[0]
    print(f"El nombre de usuario es: {nombre_de_usuario}")
else:
    print("No se encontró ningún nombre de usuario.")




conexion.close()
