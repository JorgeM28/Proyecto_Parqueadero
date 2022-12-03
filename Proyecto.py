from tkinter import *
from tkinter import messagebox

def salir():
    ventana.destroy()


def send_data():
    username_data =username.get()
    código_data =str(código.get())
    provincia_data = var_provincia.get()
    vehiculo_data = var_vehiculo.get()

    placa_data =str(placa.get())
    tiempo_data =tiempo.get()
    print("NOMBRE: ",username_data, "\t","CODIGO",código_data, "\t","TIPO DE VEHÍCULO" ,vehiculo_data, "\t","PLACA ", placa_data, "\t","LUGAR DE ESTACIONAMIENTO", provincia_data)

    newfile=open("Registros.txt", "a")
    newfile.write("NOMBRE: ")
    newfile.write(username_data)
    newfile.write("\t")
    newfile.write("CODIGO: ")
    newfile.write(código_data)
    newfile.write("\t")
    newfile.write("TIPO DE VEHICULO: ")
    newfile.write(vehiculo_data)
    newfile.write("\t")
    newfile.write("PLACA: ")
    newfile.write(placa_data)
    newfile.write("\t")
    newfile.write("LUGAR DE ESTACIONAMIENTO: ")   
    newfile.write(provincia_data)
    newfile.write("\n")
    newfile.close()
    print("Nuevo usuario registrado. NOMBRE: {} | LUGAR DE ESTACIONAMIENTO: {} ".format(username_data, tiempo_data))

    username_entry.delete(0, END)
    código_entry.delete(0, END)
    placa_entry.delete(0, END)

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


def acceder():
    global ventana_acceso, usuario_entry, contraseña_entry
    
    ventana_acceso = Toplevel()
    ventana_acceso.title("CELADOR")
    ventana_acceso.resizable(False, False)

    usuario_label = Label(ventana_acceso, text="USUARIO:")
    usuario_entry = Entry(ventana_acceso, bd=5, highlightcolor="red", highlightthickness=2)
    contraseña_label = Label(ventana_acceso, text="CONTRASEÑA:")
    contraseña_entry = Entry(ventana_acceso, bd=5, show='*', highlightcolor="red", highlightthickness=2)
    boton_aceptar = Button(ventana_acceso, text="ACEPTAR", command=aceptar)
    boton_cancelar = Button(ventana_acceso, text="CANCELAR", command=cancelar)

    usuario_label.grid(row=0, column=0, sticky= "W", padx=10, pady=10)
    usuario_entry.grid(row=0, column=1, padx=10)
    contraseña_label.grid(row=1, column=0, sticky= "W", padx=10, pady=10)
    contraseña_entry.grid(row=1, column=1, padx=10)
    boton_aceptar.grid(row=2, column=0, padx=10, pady=10, sticky= "W")
    boton_cancelar.grid(row=2, column=1, padx=10, pady=10, sticky= "E")

def cancelar():
    usuario_entry.delete(0, "end")
    contraseña_entry.delete(0, "end")

def aceptar():
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
    entry_b = Entry(frame_resultados, textvariable=borrar)
    entry_b.config(font=("Arial",20), justify=LEFT,fg="black")
    entry_b.place(x=300, y=425, width=115, height=30)
    def exit():
        ventana_sec.destroy()
    salir_btn =Button(ventana_sec, text="Salir de la ventana", command=exit, width="30", height="2")
    salir_btn.place(x=660, y=435)
    salir_borrar=Button(ventana_sec, text="Borrar dato", command=borrar_dato, width="30", height="2")
    salir_borrar.place(x=60, y=435)
    entry_b.delete(0, END)
    with open("Registros.txt") as archivo:
        for linea in archivo:
            t_resultados.insert(INSERT, linea)


def borrar_dato():
    archivo = open('Registros.txt', 'r')
    lineas = archivo.readlines()
    archivo.close()
    del lineas[int(borrar.get())-1]
    archivo = open("Registros.txt", "w")
    archivo.writelines(lineas)
    archivo.close()
  

username_label = Label(text="NOMBRE COMPLETO", bg="#FFEEDD")
username_label.place(x=22, y=70)
código_label = Label(text="CÓDIGO o CC", bg="#FFEEDD")
código_label.place(x=22, y=130)

tipodevehículo_label = Label(text="TIPO DE VEHÍCULO", bg="#FFEEDD")
tipodevehículo_label.place(x=22, y=190)

placa_label = Label(text="PLACA", bg="#FFEEDD")
placa_label.place(x=22, y=250)
tiempo_label = Label(text="LUGAR DE ESTACIONAMIENTO", bg="#FFEEDD")
tiempo_label.place(x=22, y=310)

username = StringVar()
código = StringVar()
placa = StringVar()
tipodevehículo = StringVar()
tiempo = StringVar()
var_provincia = StringVar()
var_vehiculo = StringVar()
borrar= StringVar()


provincia_menu = OptionMenu(ventana, var_provincia, "A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","A11","A12","A13","A14","A15","A16","A17","A18","A19","A20","M1", "M2","M3","M4","M5", "M6", "M7","M8","M9","M10","M11","M12")
var_provincia.set("LUGAR DE APARCAMIENTO")

vehiculo_menu = OptionMenu(ventana, var_vehiculo, "CARRO","MOTO")
var_vehiculo.set("Tipo de Vehículo")

username_entry = Entry(textvariable=username, width="40")
código_entry = Entry(textvariable=código, width="40")
placa_entry = Entry(textvariable=placa, width="40")

username_entry.place(x=22, y=100)
código_entry.place(x=22, y=160)
placa_entry.place(x=22, y=280)
vehiculo_menu.place(x= 22, y=220)
provincia_menu.place(x= 22, y=340)

submit_btn =Button(ventana, text="Cargar datos", command=send_data, width="30", height="2")
submit_btn.place(x=22, y=390)

mostrar_btn =Button(ventana, text="Acceder", command=acceder, width="10", height="2")
mostrar_btn.place(x=0, y=0)

salir_btn =Button(ventana, text="Salir de la app", command=salir, width="30", height="2")
salir_btn.place(x=478, y=390)



ventana.mainloop()