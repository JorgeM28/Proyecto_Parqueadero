from tkinter import *
from tkinter import messagebox

def salir():
    ventana.destroy()


def send_data():
    username_data =username.get()
    código_data =str(código.get())
    tipodevehículo_data =tipodevehículo.get()
    placa_data =str(placa.get())
    tiempo_data =tiempo.get()
    print("NOMBRE: ",username_data, "\t","CODIGO",código_data, "\t","TIPO DE VEHICILO" ,tipodevehículo_data, "\t","PLACA ", placa_data, "\t","LUGAR DE ESTACIONAMIENTO", tiempo_data)

    newfile=open("Registros.txt", "a")
    newfile.write("NOMBRE: ")
    newfile.write(username_data)
    newfile.write("\t")
    newfile.write("CODIGO: ")
    newfile.write(código_data)
    newfile.write("\t")
    newfile.write("TIPO DE VEHICULO: ")
    newfile.write(tipodevehículo_data)
    newfile.write("\t")
    newfile.write("PLACA: ")
    newfile.write(placa_data)
    newfile.write("\t")
    newfile.write("LUGAR DE ESTACIONAMIENTO: ")
    newfile.write(tiempo_data)
    newfile.write("\n")
    newfile.close()
    print("Nuevo usuario registrado. NOMBRE: {} | LUGAR DE ESTACIONAMIENTO: {} ".format(username_data, tiempo_data))

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
lbl =Label(ventana,text="Bienvendido a la UIS por favor ingresa tus datos y los de tu vehículo: ", font=("Cambria", 13), bg="#56cd63", fg="white", width="550", height="2")
lbl.pack()
ventana.config(bg="green")



def ventana_sec1():
    ventana_sec = Toplevel()
    ventana_sec.title("VEHICULOS EN EL PARQUEADERO")
    ventana_sec.geometry("950x500")
    ventana_sec.config(bg="green")
    frame_resultados = Frame(ventana_sec)
    frame_resultados.config(bg="white", width=930, height=480)
    frame_resultados.place(x=10, y = 10)
    t_resultados = Text(frame_resultados)
    t_resultados.config(bg="green", fg="black", font=("Arial",10))
    t_resultados.place(x=10,y=10, width=910, height= 400)
    def exit():
        ventana_sec.destroy()
    salir_btn =Button(ventana_sec, text="Salir de la ventana", command=exit, width="30", height="2")
    salir_btn.place(x=360, y=435)
    with open("Registros.txt") as archivo:
        for linea in archivo:
            t_resultados.insert(INSERT, linea)

    
    
    
username_label = Label(text="NOMBRE COMPLETO", bg="#FFEEDD")
username_label.place(x=22, y=70)
código_label = Label(text="CÓDIGO", bg="#FFEEDD")
código_label.place(x=22, y=130)
tipodevehículo_label = Label(text="TIPO DE VEHÍCULO, ¿CARRO Ó MOTO?", bg="#FFEEDD")
tipodevehículo_label.place(x=22, y=190)
placa_label = Label(text="PLACA", bg="#FFEEDD")
placa_label.place(x=22, y=250)
tiempo_label = Label(text="LUGAR DE ESTACIONAMIENTO", bg="#FFEEDD")
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

mostrar_btn =Button(ventana, text="Mostar datos", command=ventana_sec1, width="30", height="2")
mostrar_btn.place(x=250, y=390)

salir_btn =Button(ventana, text="Salir de la app", command=salir, width="30", height="2")
salir_btn.place(x=478, y=390)



ventana.mainloop()