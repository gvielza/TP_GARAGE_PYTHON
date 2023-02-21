import tkinter

window = tkinter.Tk()
window.title("garage")
window.geometry('700x700')
window.configure(bg='#333333')

frame = tkinter.Frame(bg='#333333')



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
buscar_boton = tkinter.Button(frame, text="Buscar", bg='#FF3399', fg="#FFFFFF", font=("Arial", 15))

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


frame.pack()

window.mainloop()












