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

import p4auxRegistroPATH as RP

driver=None
url="https://books.toscrape.com/"

def InicializarDriver():
    global driver
    options = Options()
    options.add_argument("--disable-popup-blocking")
    driver = uc.Chrome(options=options)
    driver.maximize_window()    
    driver.get(url)

lista_XPATH=[]

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
longitud=len(RP.coleccion_XPATH)
RP.coleccion_XPATH[f"PATH numero {longitud+1}"]={}
RP.coleccion_XPATH[f"PATH numero {longitud+1}"]["url"]=url
RP.coleccion_XPATH[f"PATH numero {longitud+1}"]["lista_XPATH"]=lista_XPATH
RP.guardar_registro()