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

# Función para guardar el diccionario de XPaths en un archivo JSON
def guardar_registro():
    with open("archivo_XPATH.json", "w") as archivo:
        json.dump(diccionario_XPATH, archivo, indent=4)

# Función para cargar el diccionario de XPaths desde el archivo JSON
def cargar_registro():
    try:
        with open("archivo_XPATH.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}  # Devuelve un diccionario vacío si el archivo no existe

diccionario_XPATH = cargar_registro()

# Función para añadir una nueva colección de XPaths al diccionario
def añadir_XPATH(nombre, lista_xpath):
    diccionario_XPATH[nombre] = lista_xpath
    guardar_registro()  # Guarda los cambios en el archivo