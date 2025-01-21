from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc

class WebLibros:
    def __init__(self, driver):
        self.driver = driver
        self.category_travel = (By.XPATH, "//a[@href='catalogue/category/books/travel_2/index.html']")
        self.campo_password = (By.ID, "password")
        self.boton_login = (By.ID, "boton-entrar")

    def realizar_login(self, password):
        self.driver.find_element(*self.category_travel).click()
        self.driver.find_element(*self.campo_password).send_keys(password)
        self.driver.find_element(*self.boton_login).click()

# Uso
driver = uc.Chrome()
driver.get("https://books.toscrape.com/")
web_libros = WebLibros(driver)
web_libros.realizar_login("mi_usuario", "mi_password")