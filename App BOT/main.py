import tkinter

#~-- MIS IMPORTACIONES --~#
from funcion_abrir_webdrivers import abrir_webdrivers
from funcion_venta import venta
#~-- MIS IMPORTACIONES --~#

def aplicacion():
    def mostrar_apartado1():
        apartado2.grid_remove()
        apartado3.grid_remove()
        apartado1.grid(row=0, column=1, padx=10, pady=10)
    def mostrar_apartado2():
        apartado1.grid_remove()
        apartado3.grid_remove()
        apartado2.grid(row=0, column=1, padx=10, pady=10)
    def mostrar_apartado3():
        apartado1.grid_remove()
        apartado2.grid_remove()
        apartado3.grid(row=0, column=1, padx=10, pady=10)

    # Crear las dos ventanas de la aplicacion
    ventana = tkinter.Tk()
    ventana.title("Bot")
    ventana.geometry("700x400")
    ventana2 = tkinter.Toplevel(ventana)
    ventana2.title("Elegir tarea")
    ventana2.geometry("400x50")

        # VENTANA2: Crear botones para cambiar entre apartados
    boton_apartado1 = tkinter.Button(
        ventana2, text="Mostrar Apartado 1", command=mostrar_apartado1)
    boton_apartado1.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    boton_apartado2 = tkinter.Button(
        ventana2, text="Mostrar Apartado 2", command=mostrar_apartado2)
    boton_apartado2.grid(row=0, column=1, padx=10, pady=10, sticky="w")
    boton_apartado3 = tkinter.Button(
        ventana2, text="Mostrar Apartado 3", command=mostrar_apartado3)
    boton_apartado3.grid(row=0, column=2, padx=10, pady=10, sticky="w")

        # VENTANA: Crear apartado 1
    apartado1 = tkinter.Frame(ventana, width=200, height=100)
    boton1_apartado1 = tkinter.Button(apartado1, text="Abrir webdrivers", command=abrir_webdrivers)
    boton1_apartado1.grid(row=0, column=0)

        # VENTANA: Crear apartado 2
    apartado2 = tkinter.Frame(ventana, width=200, height=100, bg="lightgreen")

    boton1_apartado2 = tkinter.Button(
        apartado2, text="Abrir bot de venta", command=venta)
    boton1_apartado2.grid(row=0, column=0)
    boton2_apartado2 = tkinter.Button(apartado2, text="Abrir bot de compra")
    boton2_apartado2.grid(row=0, column=1)

        # VENTANA: Crear apartado 3
    apartado3 = tkinter.Frame(ventana, width=200, height=100, bg="lightyellow")
    boton2_apartado3 = tkinter.Button(apartado3, text="Botón 2 Apartado 3")
    boton2_apartado3.grid(row=0, column=1, padx=5, pady=5)

    # Mostrar el primer apartado por defecto
    mostrar_apartado1()

    # Mostrar ventana
    ventana.mainloop()

aplicacion()