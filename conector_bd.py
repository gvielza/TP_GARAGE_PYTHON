import sqlite3
conexion = sqlite3.connect('ejemplo.db')
cursor = conexion.cursor()

#cursor.execute('''CREATE TABLE usuarios
#(id INTEGER PRIMARY KEY, usuario TEXT, contrasena TEXT)''')
#cursor.execute("INSERT INTO usuarios (usuario, contrasena, rol) VALUES (?, ?, ?)", ("geo", "admin","escritor"))
#conexion.commit()

#cursor.execute("SELECT * FROM usuarios")
#cursor.execute("DELETE  FROM usuarios")
#conexion.commit()

#resultado = cursor.fetchone()

def consultar_usuario(user):
    cursor.execute("SELECT * FROM usuarios WHERE usuario = ?", (user,))
    resultado = cursor.fetchone()
    if resultado:
        print(f"El nombre de usuario es: {resultado[1]} ,contraseña :{resultado[2]} y el rol: {resultado[3]}")
    else:
        print("El usuario no fue encontrado")

    #print(str(resultado)+ str(user))
    return resultado







def mostrar_usuarios():
    cursor.execute("SELECT * FROM usuarios")
    datos = cursor.fetchall()

    for fila in datos:
        print(fila)
mostrar_usuarios()
print(consultar_usuario("geo"))

conexion.close()
