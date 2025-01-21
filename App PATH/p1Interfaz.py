import tkinter
from tkinter import ttk
import json
import threading
import time
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import pyperclip
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options

import p0InicializarDriver as ID

def guardar_registro():
    with open("coleccion.json", "w") as archivo:
        json.dump(coleccion_XPATH, archivo, indent=4)

# Función para cargar el diccionario de XPaths desde el archivo JSON
def cargar_registro():
    try:
        with open("coleccion.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}  # Devuelve un diccionario vacío si el archivo no existe

coleccion_XPATH = cargar_registro()

#APARTADO 1
def mostrar_datos_en_tabla():
    datos = cargar_registro()
    filas = tabla.get_children("")
    for fila in filas:
        tabla.delete(fila)
    for nombre,subdiccionario in datos.items():
        tabla.insert("", "end", values=(nombre,subdiccionario["url"]))

elem=None
valo=None
nomb=None

def editar_PATH():
    global elem, valo, nomb
    seleccion=tabla.selection()
    if seleccion:
        elem=tabla.item(seleccion)
        valo=elem['values']
        nomb=valo[0]
    mostrar_datos_tabla_PATH()

def ejecutar_PATH():
    seleccion=tabla.selection()
    if seleccion:
        elemento=tabla.item(seleccion)
        valores=elemento['values']
        nombre=valores[0]
        web=valores[1]
    aux_datos=cargar_registro()
    datos=aux_datos[nombre]["lista_XPATH"]
    ID.InicializarDriver(web)
    time.sleep(15)
    for ruta in datos:
        ID.driver.find_element(By.XPATH, ruta).click()
        time.sleep(3)

"""
def eliminar_skin():
    aux_eliminadas=[]
    seleccionadas = tabla.selection()
    for seleccionada in seleccionadas:
        aux_eliminadas.append(tabla.item(seleccionada)['values'][1])
        tabla.delete(seleccionada)
        for i in range(len(aux_eliminadas)):
            try:
                if aux_eliminadas[i] in lista_XPATH:
                    lista_XPATH.remove(aux_eliminadas[i])
            except ValueError:
                pass  
    guardar_registro()
"""
#

#APARTADO 2
def mostrar_datos_tabla_PATH():
    global elem, valo, nomb
    aux_datos=cargar_registro()
    datos=aux_datos[nomb]["lista_XPATH"]
    filas = tabla_PATH.get_children("")
    for fila in filas:
        tabla_PATH.delete(fila)
    for xpath in datos:
        tabla_PATH.insert("", "end", values=(xpath))
#

#APARTADO 3
def guardar_PATH():
    nombre=entrada1_apartado3.get()
    url=entrada2_apartado3.get()
    descripcion=texto1_apartado3.get("1.0", tkinter.END)
    if url and descripcion:
        coleccion_XPATH[nombre]={
            "url":url,
            "descripcion":descripcion,
            "lista_XPATH":""
        }
    elif url:
        coleccion_XPATH[nombre]={
            "url":url,
            "descripcion":"",
            "lista_XPATH":""
        }
    else:
        print("Es necesario proporcionar una URL.")
    entrada1_apartado3.delete(0,tkinter.END)
    entrada2_apartado3.delete(0,tkinter.END)
    texto1_apartado3.delete("1.0", tkinter.END)
    guardar_registro()
    mostrar_datos_en_tabla()

"""
def mostrar_datos_en_tabla_PATH():
    seleccion=tabla.selection()
    if seleccion:
        elemento=tabla.item(seleccion)
        valores=elemento['values']
        nombre=valores[0]
    aux_datos=cargar_registro()
    datos=aux_datos[nombre]["lista_XPATH"]
    filas = tabla_PATH.get_children("")
    for fila in filas:
        tabla_PATH.delete(fila)
    for xpath in datos:
        tabla_PATH.insert("", "end", values=(xpath))
"""
#

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

ventana2 = tkinter.Tk()
ventana2.title("Elegir tarea")
ventana2.geometry("400x50")

ventana = tkinter.Tk()
ventana.title("Registro")
ventana.geometry("700x400")

# Crear botones para cambiar entre apartados
boton_apartado1 = tkinter.Button(
    ventana2, text="Mostrar Apartado 1", command=mostrar_apartado1)
boton_apartado1.grid(row=0, column=0, padx=10, pady=10, sticky="w")
boton_apartado2 = tkinter.Button(
    ventana2, text="Mostrar Apartado 2", command=mostrar_apartado2)
boton_apartado2.grid(row=0, column=1, padx=10, pady=10, sticky="w")
boton_apartado3 = tkinter.Button(
    ventana2, text="Mostrar Apartado 3", command=mostrar_apartado3)
boton_apartado3.grid(row=0, column=2, padx=10, pady=10, sticky="w")

# Crear apartado 1
apartado1 = tkinter.Frame(ventana, width=200, height=100)

tabla = ttk.Treeview(apartado1)
tabla['columns']=('Nombre','URL')#('Paso','Tipo','Información')

    # Ocultar la columna #0 (jerárquica) que aparece por defecto
tabla.column("#0", width=0, stretch=tkinter.NO)
tabla.heading("#0", text="")

    # Configurar las cabeceras de las columnas
tabla.column("Nombre", anchor=tkinter.W, width=150)
tabla.column("URL", anchor=tkinter.W, width=300)

    # Asignar los encabezados
tabla.heading("Nombre", text="Nombre", anchor=tkinter.W)
tabla.heading("URL", text="URL", anchor=tkinter.W)
tabla.grid(row=2, column=1, columnspan=3, padx=5, pady=5)

boton1 = tkinter.Button(apartado1, text="Editar PATH",command=editar_PATH)
boton1.grid(row=1, column=1, padx=5, pady=5, sticky="w")
boton2 = tkinter.Button(apartado1, text="Ejecutar PATH",command=ejecutar_PATH)
boton2.grid(row=1, column=2, padx=5, pady=5, sticky="w")
boton3 = tkinter.Button(
    apartado1, text="Eliminar PATH")
boton3.grid(row=1, column=3, padx=5, pady=5, sticky="w")

# Crear apartado 2
apartado2 = tkinter.Frame(ventana, width=200, height=100)

boton1_apartado2 = tkinter.Button(
    apartado2, text="Abrir bot de venta")
boton1_apartado2.grid(row=0, column=0)
boton2_apartado2 = tkinter.Button(apartado2, text="Añadir paso")
boton2_apartado2.grid(row=0, column=1)
boton2_apartado2 = tkinter.Button(apartado2, text="Eliminar paso")
boton2_apartado2.grid(row=0, column=2)

    #Mostrar el PATH en tabla
tabla_PATH = ttk.Treeview(apartado2)
tabla_PATH['columns']=('XPATH')

    # Ocultar la columna #0 (jerárquica) que aparece por defecto
tabla_PATH.column("#0", width=0, stretch=tkinter.NO)
tabla_PATH.heading("#0", text="")

    # Configurar las cabeceras de las columnas
tabla_PATH.column("XPATH", anchor=tkinter.W, width=300)

    # Asignar los encabezados
tabla_PATH.heading("XPATH", text="XPATH", anchor=tkinter.W)
tabla_PATH.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

# Crear apartado 3
apartado3 = tkinter.Frame(ventana, width=200, height=100)

etiqueta1_apartado3 = tkinter.Label(apartado3, text="Nombre del PATH:")
etiqueta1_apartado3.grid(row=0, column=0, sticky="w")
entrada1_apartado3 = tkinter.Entry(apartado3)
entrada1_apartado3.grid(row=0, column=1, padx=5, pady=5, sticky="w")
etiqueta2_apartado3 = tkinter.Label(apartado3, text="URL del sitio web:")
etiqueta2_apartado3.grid(row=1, column=0, sticky="w")
entrada2_apartado3 = tkinter.Entry(apartado3)
entrada2_apartado3.grid(row=1, column=1, padx=5, pady=5, sticky="w")
etiqueta2_apartado3 = tkinter.Label(apartado3, text="Descripción:")
etiqueta2_apartado3.grid(row=2, column=0, sticky="w")
texto1_apartado3 = tkinter.Text(apartado3, height=10, width=60)
texto1_apartado3.grid(row=3, column=0, rowspan=1, columnspan=3, sticky="nsew", padx=10, pady=10)
boton1_apartado3 = tkinter.Button(apartado3, text="Guardar PATH",command=guardar_PATH)
boton1_apartado3.grid(row=4, column=1, padx=5, pady=5)

# Mostrar el primer apartado por defecto
mostrar_apartado1()
mostrar_datos_en_tabla()
guardar_registro()

# Mostrar ventana
ventana.mainloop()