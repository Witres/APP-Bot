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
import json
import csv

# Función para guardar el diccionario de XPaths en un archivo JSON
def guardar_archivo_XPATH():
    with open("archivo_XPATH.json", "w") as archivo:
        json.dump(diccionario_XPATH, archivo, indent=4)

# Función para cargar el diccionario de XPaths desde el archivo JSON
def cargar_archivo_XPATH():
    try:
        with open("archivo_XPATH.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}  # Devuelve un diccionario vacío si el archivo no existe

lista_XPATH=[]
diccionario_XPATH = cargar_archivo_XPATH()

# Función para añadir una nueva colección de XPaths al diccionario
def añadir_XPATH(nombre, ruta):
    diccionario_XPATH[nombre] = ruta
    guardar_archivo_XPATH()  # Guarda los cambios en el archivo

driver=None

def InicializarDriver():
    global driver
    options = Options()
    options.add_argument("--disable-popup-blocking")
    driver = uc.Chrome(options=options)
    driver.maximize_window()    
    driver.get("https://books.toscrape.com/")

def AlmacenarClick():
    global driver

    # Inyectar un script JavaScript en la página que capture los clics
    driver.execute_script("""
    document.addEventListener('contextmenu', function(event) {
        //event.preventDefault(); Evitar el comportamiento por defecto, como seguir un enlace
        window.clickedElement = event.target;
        console.log('Elemento clickeado:', window.clickedElement.tagName);
    }, true);
    """)
    print("Haz clic en cualquier elemento de la página dentro de los próximos 15 segundos...")
    time.sleep(5)

    # Recuperar el elemento clickeado
    clicked_element = driver.execute_script("return window.clickedElement;")

    # Obtener información del elemento clickeado y construir el XPATH
    tag_name = driver.execute_script("return window.clickedElement.tagName;").lower()
    atributos = driver.execute_script("""
    let elem = window.clickedElement;
    if (!elem) return null;
    let attrs = elem.attributes;
    let result = {};
    for (let i = 0; i < attrs.length; i++) {
        result[attrs[i].name] = attrs[i].value;
    }
    return result;
    """)
    pre_XPATH="//"+tag_name+"["
    if atributos:
        print("Atributos del elemento clickeado:")
        for nombre, valor in atributos.items():
            pre_XPATH=pre_XPATH+"@"+nombre+"='"+valor+"' and "
            print(f"Atributo: {nombre}, Valor: {valor}")
    else:
        print("No se ha encontrado ningún elemento clickeado o el elemento no tiene atributos.")
    print("Etiqueta del elemento clickeado con botón derecho:", tag_name)
    texto = driver.execute_script("return window.clickedElement.textContent;").strip()
    if texto:
        print("Texto del elemento:", texto)
        XPATH=pre_XPATH+"contains(text(),'"+texto+"')]"
    if atributos:
        pre_XPATH=pre_XPATH.split()
        del pre_XPATH[-1]
        pre_XPATH=" ".join(pre_XPATH)
        XPATH=pre_XPATH+"]"
    else:
        print("No se ha podido obtener información del elemento clickado.")
    lista_XPATH.append(XPATH)
    driver.find_element(By.XPATH, XPATH).click()
InicializarDriver()
Npasos=int(input("Indique el número de pasos que tendrá el proceso:"))
for i in range(Npasos):
    AlmacenarClick()
longitud_diccionario=len(diccionario_XPATH)
añadir_XPATH(f"XPATH numero {longitud_diccionario+1}", lista_XPATH)