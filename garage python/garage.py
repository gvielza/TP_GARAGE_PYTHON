import tkinter
import sqlite3
import csv
from datetime import datetime
conexion= sqlite3.connect("garage_db")
cursor = conexion.cursor()

window = tkinter.Tk()
window.title("garage")
window.geometry('750x750')
window.configure(bg='#333333')

frame = tkinter.Frame(bg='#333333')


def pagar_servicio():
    patente= patente_entrada.get()
    cursor.execute('SELECT * FROM movimientos where patente=?',(patente,))
    resultado = cursor.fetchone()
    if resultado is not None and resultado[4]=="":
        estado_actual= "pagado"
        cursor.execute('UPDATE movimientos SET estado=? WHERE patente=?',(estado_actual,patente))
        conexion.commit()
        print("servicio pagado")




def buscar_patente():
    patente= patente_entrada.get()
    cursor.execute('SELECT * FROM movil where patente=?',(patente,))
    resultado = cursor.fetchone()
    salida= salida_entrada.get()


    if resultado is not None:
        marca_entrada.insert(0,resultado[1])
        modelo_entrada.insert(0,resultado[2])
        color_entrada.insert(0,resultado[3])
        cursor.execute('SELECT * FROM movimientos where patente=?',(patente,))
        resultado2= cursor.fetchone()
        marca_entrada.config(state="disabled")
        modelo_entrada.config(state="disabled")
        color_entrada.config(state="disabled")
        if resultado2 is not None: 
            print(resultado2)
            print(resultado2[3])
            entrada_entrada.insert(0,resultado2[1])
            salida_entrada.insert(0,resultado2[2])

            if resultado2[4]=="":
                pagar_boton.config(state="normal")
            else:
                pagar_boton.config(state="disabled")
            #if resultado2[3]=="":
                #salir_boton.config(state="normal")
        else:
            print("No tiene fecha de entrada")
    else: 
        print("El auto no esta en el garage")
        entrar_boton.config(state="normal")



def guardar_auto():
    salida= ""
    patente= patente_entrada.get()
    marca = marca_entrada.get()
    modelo = modelo_entrada.get()
    color = color_entrada.get()
    entrada = datetime.now()
    cursor.execute('INSERT INTO movil (patente,marca,modelo,color,observaciones)VALUES(?,?,?,?,?)',(patente,marca,modelo,color,""))
    cursor.execute('INSERT INTO movimientos (patente,fechahora_entrada,fechahora_salida,observaciones,estado)VALUES(?,?,?,?,?)',(patente,entrada,salida,"",""))
    conexion.commit()
    print("Guardado exitosamente")


def salir_garage():

    salida = datetime.now()
    patente= patente_entrada.get()
    cursor.execute('UPDATE movimientos SET fechahora_salida=? WHERE patente=?',(salida,patente))
    conexion.commit()
    print("Salio del garage")


def exportar_datos():
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    cursor.execute('SELECT * from movimientos')
    movimientos = cursor.fetchall()
    print(usuarios)
    print(movimientos)

    with open("usuarios.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre","Usuario", "Contraseña", "Tipo de usuario"])
        writer.writerows(usuarios)
    

    with open("movimientos.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Patente","Fecha y hora de entrada", "Fecha y hora de salida", "Observaciones","Estado"])
        writer.writerows(movimientos)



def importar_datos():
    with open ("usuarios.csv", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        usuarios = [row for row in reader]
        print(usuarios)


    with open ("movimientos.csv", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        usuarios = [row for row in reader]
        print(usuarios)


def modificar_datos():
    patente = patente_entrada.get()
    entrada = entrada_entrada.get()
    salida = salida_entrada.get()
    cursor.execute('UPDATE movimientos SET fechahora_entrada=?,fechahora_salida=? where patente=? ',(entrada,salida,patente))
    conexion.commit()
    print("Se modificaron los datos")
    





#diseño de los textos
garage_label = tkinter.Label(frame, text="Garage", bg='#333333', fg="#FFFFFF",font=("Arial",25))
patente_label = tkinter.Label(frame, text="Patente", bg='#333333', fg="#FFFFFF", font=("Arial, 15"))
patente_entrada = tkinter.Entry(frame)
marca_label = tkinter.Label(frame, text="Marca", bg='#333333', fg="#FFFFFF", font=("Arial", 15))
marca_entrada = tkinter.Entry(frame)
modelo_label = tkinter.Label(frame, text="Modelo", bg='#333333', fg="#FFFFFF", font=("Arial", 15))
modelo_entrada = tkinter.Entry(frame)
color_label = tkinter.Label(frame, text="Color", bg='#333333', fg="#FFFFFF", font=("Arial", 15))
color_entrada = tkinter.Entry(frame)
entrada_label = tkinter.Label(frame, text="Entrada", bg='#333333', fg="#FFFFFF", font=("Arial", 15))
entrada_entrada = tkinter.Entry(frame)
salida_label = tkinter.Label(frame, text="Salida", bg='#333333', fg="#FFFFFF", font=("Arial", 15))
salida_entrada = tkinter.Entry(frame)
pagar_boton = tkinter.Button(frame, text="Pagar", bg='#FF3399', fg="#FFFFFF", font=("Arial", 15),command=pagar_servicio)
entrar_boton = tkinter.Button(frame, text="entrar", bg='#FF3399', fg="#FFFFFF", font=("Arial", 15),command=guardar_auto)
salir_boton = tkinter.Button(frame, text="salir", bg='#FF3399', fg="#FFFFFF", font=("Arial", 15),command=salir_garage)
importar_boton = tkinter.Button(frame, text="Importar datos", bg='#FF3399', fg="#FFFFFF", font=("Arial", 15,),command=importar_datos)
exportar_boton = tkinter.Button(frame, text="Exportar datos", bg='#FF3399', fg="#FFFFFF", font=("Arial", 15), command=exportar_datos)
modificar_boton = tkinter.Button(frame, text="Modificar datos", bg='#FF3399', fg="#FFFFFF", font=("Arial", 15), command=modificar_datos)
buscar_boton = tkinter.Button(frame, text="Buscar", bg='#FF3399', fg="#FFFFFF", font=("Arial", 15),command=buscar_patente)

#posicion de los textos y botones
garage_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=25)
patente_label.grid(row=1 , column=0)
patente_entrada.grid(row=1 , column=1, pady=20)
marca_label.grid(row=2, column=0)
marca_entrada.grid(row=2, column=1, pady=20)
modelo_label.grid(row=3, column=0)
modelo_entrada.grid(row=3,column=1, pady=20)
color_label.grid(row=4,column=0, pady=20)
color_entrada.grid(row=4,column=1, pady=20)
entrada_label.grid(row=5,column=0, pady=20)
entrada_entrada.grid(row=5,column=1, pady=20)
salida_label.grid(row=6,column=0, pady=20)
salida_entrada.grid(row=6,column=1, pady=20)
pagar_boton.grid(row=7, column=0, columnspan=2, pady=25)
entrar_boton.grid(row=7, column=1, columnspan=2, pady=25)
salir_boton.grid(row=7, column=2, columnspan=2, pady=25)
exportar_boton.grid(row=8, column=2, columnspan=2, pady=25)
importar_boton.grid(row=8, column=0, columnspan=2, pady=25)
modificar_boton.grid(row=10, column=0, columnspan=2, pady=25)
buscar_boton.grid(row=1 , column=2, pady=20)

##deshabilitar botones
salir_boton.config(state="disabled")
entrar_boton.config(state="disabled")

frame.pack()

window.mainloop()












