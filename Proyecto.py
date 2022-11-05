from tkinter import *

def send_data():
    username_data =username.get()
    código_data =str(código.get())
    tipodevehículo_data =tipodevehículo.get()
    placa_data =str(placa.get())
    tiempo_data =tiempo.get()
    print(username_data, "\t", código_data, "\t", tipodevehículo_data, "\t", placa_data, "\t", tiempo_data)

    newfile=open("Registros.txt", "a")
    newfile.write(username_data)
    newfile.write("\t")
    newfile.write(código_data)
    newfile.write("\t")
    newfile.write(tipodevehículo_data)
    newfile.write("\t")
    newfile.write(placa_data)
    newfile.write("\t")
    newfile.write(tiempo_data)
    newfile.write("\n")
    newfile.close()
    print("Nuevo usuario registrado. NOMBRE: {} | TIEMPO: {} ".format(username_data, tiempo_data))

    username_entry.delete(0, END)
    código_entry.delete(0, END)
    tipodevehículo_entry.delete(0, END)
    placa_entry.delete(0, END)
    tiempo_entry.delete(0, END)

ventana = Tk()
ventana.title("Registro del usuario para ingresar al parqueadero")
ventana.geometry("800x500")

logo=PhotoImage(file="img/download.png")
lb_logo = Label(image=logo)
lb_logo.place(x=480,y=150)

ventana.resizable(False,False)
ventana.config(background="#E8EAEC")
lbl =Label(ventana,text="Hola bienvendido a la UIS por favor ingresa tus datos y los de tu vehículo: ", font=("Cambria", 13), bg="#56cd63", fg="white", width="550", height="2")
lbl.pack()
ventana.config(bg="green")



username_label = Label(text="NOMBRE COMPLETO", bg="#FFEEDD")
username_label.place(x=22, y=70)
código_label = Label(text="CÓDIGO", bg="#FFEEDD")
código_label.place(x=22, y=130)
tipodevehículo_label = Label(text="TIPO DE VEHÍCULO", bg="#FFEEDD")
tipodevehículo_label.place(x=22, y=190)
placa_label = Label(text="PLACA", bg="#FFEEDD")
placa_label.place(x=22, y=250)
tiempo_label = Label(text="TIEMPO DE ESTADÍA EN EL PARQUEADERO", bg="#FFEEDD")
tiempo_label.place(x=22, y=310)

username = StringVar()
código = StringVar()
tipodevehículo = StringVar()
placa = StringVar()
tiempo = StringVar()

username_entry = Entry(textvariable=username, width="40")
código_entry = Entry(textvariable=código, width="40")
tipodevehículo_entry = Entry(textvariable=tipodevehículo, width="40")
placa_entry = Entry(textvariable=placa, width="40")
tiempo_entry = Entry(textvariable=tiempo, width="40")

username_entry.place(x=22, y=100)
código_entry.place(x=22, y=160)
tipodevehículo_entry.place(x=22, y=220)
placa_entry.place(x=22, y=280)
tiempo_entry.place(x=22, y=340)

submit_btn =Button(ventana, text="Cargar datos", command=send_data, width="30", height="2")
submit_btn.place(x=22, y=390)

ventana.mainloop()