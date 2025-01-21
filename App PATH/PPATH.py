# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 20:35:20 2024

@author: salva
"""

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

options = Options()
options.add_argument("--disable-popup-blocking")
driver = uc.Chrome(options=options)
driver.maximize_window()
driver.get("https://www.google.com")

driver=None

#INICIALIZAR WEBDRIVERS

#FUNCION CAPTURAR CLICKS Y REALIZAR CLICKS

#FUNCION ESCRIBIR

#BOTONES(click,escribir,crear path,añadir paso al path)

#EDITAR UN PATH YA CREADO