import sqlite3

conexion = sqlite3.connect("garage_db")
cursor = conexion.cursor()
#cursor.execute('''CREATE TABLE usuarios
#(nombre TEXT,usuario TEXT, contrasena TEXT, tipo_de_usuario TEXT)''')

#cursor.execute('INSERT INTO usuarios (nombre, usuario, contrasena, tipo_de_usuario) VALUES(?,?,?,?)',("Franco","fs123","hola123","user"))
#conexion.commit()

def eliminar_usuarios():
    cursor.execute("DELETE  FROM usuarios")
    conexion.commit()
    print("limpiada la tbla")

def mostrar_usuarios():
    cursor.execute("SELECT * FROM  usuarios")
    datos=cursor.fetchall()

    for fila in datos:
        print(fila)



mostrar_usuarios()
#eliminar_usuarios()
#mostrar_usuarios()


