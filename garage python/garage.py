import tkinter

import sqlite3

conexion = sqlite3.connect("garage_db")
cursor = conexion.cursor()

window = tkinter.Tk()
window.title("garage")
window.geometry('700x700')
window.configure(bg='#333333')

frame = tkinter.Frame(bg='#333333')

def buscar_movile():
    cursor.execute("SELECT * FROM moviles WHERE patente = ?", (patente_entrada.get(),))
    resultado = cursor.fetchone()
    if resultado is not None:
        print("está el auto")
        marca_entrada.insert(0,resultado[1])
        modelo_entrada.insert(0,resultado[2])
        color_entrada.insert(0,resultado[3])
        cursor.execute("SELECT * FROM movimientos WHERE patente = ?", (patente_entrada.get(),))
        mov=cursor.fetchone()
        if mov is not None:
            print("si mov")
            entrada_entrada.insert(0,mov[1])
            salida_entrada.insert(0,mov[2])
        else:
            print("no esta")


    else:
        print("no eeeesta el auto")
        boton_entrar.config(bg="red")

def insertar_datos():
    cursor.execute('INSERT INTO moviles (patente, marca, modelo, color, observaciones) VALUES(?,?,?,?,?)',
                   (patente_entrada.get(), marca_entrada.get(), modelo_entrada.get(), color_entrada.get(), ""))

    cursor.execute('INSERT INTO movimientos (patente, fechahora_entrada, fechahora_salida, lugar) VALUES(?,?,?,?)',(patente_entrada.get(),entrada_entrada.get(),"",""))
    conexion.commit()
    window.update()


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
pagar_boton = tkinter.Button(frame, text="Pagar", bg='#FF3399', fg="#FFFFFF", font=("Arial", 15))
importar_boton = tkinter.Button(frame, text="Importar datos", bg='#FF3399', fg="#FFFFFF", font=("Arial", 15))
exportar_boton = tkinter.Button(frame, text="Exportar datos", bg='#FF3399', fg="#FFFFFF", font=("Arial", 15))
buscar_boton = tkinter.Button(frame, text="Buscar", bg='#FF3399', fg="#FFFFFF", font=("Arial", 15),command=buscar_movile)

boton_entrar = tkinter.Button(frame, text="Entrar", bg='#707B7C', fg="#FFFFFF", font=("Arial", 15),command=insertar_datos)

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
exportar_boton.grid(row=8, column=2, columnspan=2, pady=25)
importar_boton.grid(row=8, column=0, columnspan=2, pady=25)
buscar_boton.grid(row=1 , column=2, pady=20)

boton_entrar.grid(row=7, column=2, columnspan=2, pady=25)






frame.pack()

window.mainloop()












