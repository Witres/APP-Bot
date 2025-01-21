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

driver=None

def InicializarDriver(web):
    global driver
    options = Options()
    options.add_argument("--disable-popup-blocking")
    driver = uc.Chrome(options=options)
    driver.maximize_window()    
    driver.get(web)