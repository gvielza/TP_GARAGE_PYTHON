import sqlite3

conexion = sqlite3.connect("garage_db")
cursor = conexion.cursor()
#cursor.execute('''CREATE TABLE moviles
#(patente TEXT,marca TEXT, modelo TEXT, color TEXT, observaciones TEXT)''')
#cursor.execute('''CREATE TABLE movimientos
#(patente TEXT,fechahora_entrada TEXT, fechahora_salida TEXT, lugar TEXT)''')

#cursor.execute('INSERT INTO usuarios (nombre, usuario, contrasena, tipo_de_usuario) VALUES(?,?,?,?)',("Franco","fs123","hola123","user"))
#cursor.execute('INSERT INTO moviles (patente, marca, modelo, color, observaciones) VALUES(?,?,?,?,?)',("AB123CD","ford","focus","azul","nice"))
#cursor.execute('INSERT INTO movimientos (patente, fechahora_entrada, fechahora_salida, lugar) VALUES(?,?,?,?)',("AB123CD","22-2-23","22-2-23","bs as"))

#cursor.execute("DROP TABLE movimientos")

conexion.commit()

def eliminar_usuarios():
    cursor.execute("DELETE  FROM usuarios")
    conexion.commit()
    print("limpiada la tbla")

def mostrar_usuarios():
    cursor.execute("SELECT * FROM  usuarios")
    datos=cursor.fetchall()

    for fila in datos:
        print(fila)
def mostrar_moviles():
    cursor.execute("SELECT * FROM  moviles")
    datos=cursor.fetchall()

    for fila in datos:
        print(fila)

def mostrar_movimientos():
    cursor.execute("SELECT * FROM  movimientos")
    datos=cursor.fetchall()

    for fila in datos:
        print(fila)

def buscar_movile(patente):
    cursor.execute("SELECT * FROM moviles WHERE patente = ?", (patente,))
    resultado = cursor.fetchone()
    if resultado is not None:
        print("está el auto")
    else:
        print("no eeeesta el auto")


#mostrar_usuarios()
#eliminar_usuarios()

mostrar_moviles()
mostrar_movimientos()



