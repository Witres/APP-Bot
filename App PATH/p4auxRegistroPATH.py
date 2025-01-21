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

# Función para añadir una nueva colección de XPaths al diccionario
def añadir_XPATH(nombre, url, lista_XPATH):
    coleccion_XPATH[nombre] = {
        "url":url,
        "descripcion":"",
        "lista_XPATH":lista_XPATH
    }
    guardar_registro()  # Guarda los cambios en el archivo