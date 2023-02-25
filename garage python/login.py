import tkinter
from tkinter import messagebox
import sqlite3
conexion = sqlite3.connect("garage_db")
cursor = conexion.cursor()



def validar_datos():
    nombre = nombre_entrada.get()
    usuario= user_entrada.get()
    contrasena= password_entrada.get()
    tipo_usuario = tipo_entrada.get()
    cursor.execute('SELECT * FROM usuarios WHERE usuario=?',(usuario,))
    resultado = cursor.fetchone()
    print(resultado)

    if resultado is not None and contrasena==resultado[2] and tipo_usuario=='admin': 
        window.destroy()
        import garage
    else:
        print('Los datos ingresados son incorrectos')



def guardar_datos():
    nombre = nombre_entrada.get()
    usuario = user_entrada.get()
    contrasena = password_entrada.get()
    tipo_usuario= tipo_entrada.get()
    cursor.execute('INSERT INTO usuarios (nombre, usuario, contrasena, tipo_de_usuario) VALUES(?,?,?,?)',(nombre,usuario,contrasena,tipo_usuario))
    conexion.commit()  
    print("Se guardaron los datos")

window = tkinter.Tk()
window.title("Usuarios")
window.geometry('450x450')
window.configure(bg='#333333')
frame = tkinter.Frame(bg='#333333')



login_label = tkinter.Label(frame, text="Login", bg='#333333', fg="#FFFFFF", font=("Arial, 15"))
nombre_label = tkinter.Label(frame, text="Nombre", bg='#333333', fg="#FFFFFF", font=("Arial, 15"))
nombre_entrada = tkinter.Entry(frame)
user_label = tkinter.Label(frame, text="usuario", bg='#333333', fg="#FFFFFF", font=("Arial, 15"))
user_entrada = tkinter.Entry(frame)
password_label = tkinter.Label(frame, text="contraseña", bg='#333333', fg="#FFFFFF", font=("Arial, 15"))
password_entrada = tkinter.Entry(frame)
tipo_label = tkinter.Label(frame, text="Tipo de usuario", bg='#333333', fg="#FFFFFF", font=("Arial, 15"))
tipo_entrada = tkinter.Entry(frame)
login_boton = tkinter.Button(frame, text="Login", bg='#FF3399', fg="#FFFFFF", font=("Arial", 15),command=validar_datos)



login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=25)
nombre_label.grid(row=1 , column=0)
nombre_entrada.grid(row=1 , column=1, pady=20)
user_label.grid(row=2 , column=0)
user_entrada.grid(row=2 , column=1, pady=20)
password_label.grid(row=3 , column=0)
password_entrada.grid(row=3 , column=1, pady=20)
tipo_label.grid(row=4 , column=0)
tipo_entrada.grid(row=4 , column=1, pady=20)
login_boton.grid(row=5 , column=1, pady=20)




                      



frame.pack()

window.mainloop()