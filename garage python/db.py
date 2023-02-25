import sqlite3
conexion = sqlite3.connect("garage_db")
cursor = conexion.cursor()

#cursor.execute('''CREATE TABLE usuarios
#(nombre TEXT,usuario TEXT, contrasena TEXT, tipo_de_usuario TEXT)''')

#cursor.execute('''CREATE TABLE movimientos
#(patente TEXT,fechahora_entrada DATETIME, fechahora_salida DATETIME, observaciones TEXT, lugar TEXT)''')

#cursor.execute('INSERT INTO movimientos (patente, fechahora_entrada, fechahora_salida, lugar) VALUES(?,?,?,?)',("zrt890","22/5 16hs","23/5 14hs","garage"))
#conexion.commit()

#cursor.execute('''CREATE TABLE movil
#(patente TEXT, marca TEXT, modelo TEXT, color TEXT, observaciones TEXT)''')

#cursor.execute('INSERT INTO movil (patente, marca, modelo, color, observaciones) VALUES(?,?,?,?,?)',("zrt890","toyota","corolla","gris","Se realizo el service correctamente"))
#conexion.commit()

#cursor.execute('INSERT INTO usuarios (nombre, usuario, contrasena, tipo_de_usuario) VALUES(?,?,?,?)',("Franco","fs123","hola123","user"))
#conexion.commit()

#cursor.execute('INSERT INTO usuarios (nombre, usuario, contrasena, tipo_de_usuario) VALUES(?,?,?,?)',("Jorge","js32","123","admin"))
#conexion.commit()

#cursor.execute('''CREATE TABLE movimientos
#(patente TEXT,fechahora_entrada DATETIME, fechahora_salida DATETIME, observaciones TEXT, estado TEXT)''')

#cursor.execute('INSERT INTO movimientos (patente, fechahora_entrada, fechahora_salida, observaciones, estado) VALUES(?,?,?,?,?)',("zrt890","22/5 16hs","23/5 14hs","El service se realizo correctamente",""))
#conexion.commit()


#cursor.execute('DROP TABLE movimientos')
#conexion.commit()

def mostrar_usuarios():
    cursor.execute("SELECT * FROM  usuarios")
    datos=cursor.fetchall()

    for fila in datos:
        print(fila)
mostrar_usuarios()


def mostrar_movimientos():
    cursor.execute("SELECT * FROM  movimientos")
    datos=cursor.fetchall()

    for fila in datos:
        print(fila)
#mostrar_movimientos()

def mostrar_movil():
    cursor.execute("SELECT * FROM  movil")
    datos=cursor.fetchall()

    for fila in datos:
        print(fila)
#mostrar_movil()




