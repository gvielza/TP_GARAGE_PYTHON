from tkinter import *
from tkinter import messagebox

import conector_bd



print("hola")
ventana = Tk()
ventana.geometry("300x200")
ventana.title("Iniciar sesión")

usuario_label = Label(ventana, text="Usuario:")
usuario_label.place(x=50, y=50)
usuario_entry = Entry(ventana)
usuario_entry.place(x=110, y=50)

contrasena_label = Label(ventana, text="Contraseña:")
contrasena_label.place(x=30, y=80)
contrasena_entry = Entry(ventana, show="*")
contrasena_entry.place(x=110, y=80)

def validar_credenciales():
    usuario = usuario_entry.get()
    contrasena = contrasena_entry.get()

    if usuario == "admin" and contrasena == "admin123":
        messagebox.showinfo("Login correcto", "Bienvenido " + usuario + "!")
        ventana.destroy()
        ventana_garage=Tk()
        ventana_garage.geometry("500x200")
        ventana_garage.title("G A R A G E")
        label_inicio=Label(ventana_garage,text="—---------------------------------------------------------------------------------------")
        label_inicio.place(x=10,y=10)
        ventana_garage.mainloop()

    else:
        messagebox.showerror("Error de login", "Credenciales incorrectas")
boton = Button(ventana, text="Iniciar sesión", command=validar_credenciales)
boton.place(x=130, y=120)
ventana.mainloop()

conector_bd.mostrar_usuarios()



