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

import p2AlmacenarClick as AC

#OTRA OPCION: INICIAR UNA NUEVA INSTANCIA DE WEBDRIVER DONDE REALIZAR EL PATH
"""
options = Options()
options.add_argument("--disable-popup-blocking")
driver1 = uc.Chrome(options=options)
driver1.maximize_window()    
driver1.get("https://books.toscrape.com/")
wait1=WebDriverWait(driver1, 15)
"""

def realizar_click():
    AC.driver.get("https://books.toscrape.com/")
    time.sleep(15)
    print("Van a comenzar los clicks.")
    for ruta in AC.lista_XPATH:
        AC.driver.find_element(By.XPATH, ruta).click()
        time.sleep(3)
realizar_click()