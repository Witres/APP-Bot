import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

#~-- MIS IMPORTACIONES --~#
import funcion_abrir_webdrivers as AWD
#~-- MIS IMPORTACIONES --~#

def esperar_venta():
    while True:
        try:
            AWD.wait1.until(EC.visibility_of_element_located(
                (By.XPATH, "//div[@class='cdk-global-overlay-wrapper']//div[@class='cdk-overlay-pane' and contains(@id, 'cdk-overlay-')]//h1[contains(text(), 'Trade Found')]")))
            break
        except TimeoutException:
            AWD.driver1.refresh()
            """
            Aqui seria conveniente añadir una instancia para cerrar cuadros que se abran al recargar la pagina
            Abrir una pestaña en driver3 y, usando url=f"https://steamcommunity.com/tradeoffer/{trade_offer_ID}}/", ir comprobando si esta activo. id=f"tradeofferid_{trade_offer_ID}"
            """

def venta_ventana0():
    vender0 = AWD.driver1.find_element(
        By.XPATH, "//div[@class='cdk-global-overlay-wrapper']//div[@class='cdk-overlay-pane' and contains(@id, 'cdk-overlay-')]//h1[contains(text(), 'Trade Found')]")

    AWD.wait1.until(EC.visibility_of_element_located(
        (By.XPATH, "//div[@class='cdk-global-overlay-wrapper']//div[@class='cdk-overlay-pane' and contains(@id, 'cdk-overlay-')]//button[contains(@class, 'mat-focus-indicator w-100 mat-button-3d mat-button-lg mat-flat-button mat-button-base mat-accent')]")))
    boton_vender0 = AWD.driver1.find_element(
        By.XPATH, "//div[@class='cdk-global-overlay-wrapper']//div[@class='cdk-overlay-pane' and contains(@id, 'cdk-overlay-')]//button[contains(@class, 'mat-focus-indicator w-100 mat-button-3d mat-button-lg mat-flat-button mat-button-base mat-accent')]")
    AWD.driver1.execute_script("arguments[0].click();", boton_vender0)

def venta_ventana1():
    AWD.wait1.until(EC.visibility_of_element_located(
        (By.XPATH, "//div[@class='cdk-global-overlay-wrapper' and @style='justify-content: center; align-items: center;']//div[contains(@id,'cdk-overlay-') and @class='cdk-overlay-pane']//h1[contains(text(), 'Complete Trade')]")))
    vender1 = AWD.driver1.find_element(
        By.XPATH, "//div[@class='cdk-global-overlay-wrapper' and @style='justify-content: center; align-items: center;']//div[contains(@id,'cdk-overlay-') and @class='cdk-overlay-pane']//h1[contains(text(), 'Complete Trade')]")

    AWD.wait1.until(EC.visibility_of_element_located(
        (By.XPATH, "//div[@class='cdk-global-overlay-wrapper' and @style='justify-content: center; align-items: center;']//div[contains(@id,'cdk-overlay-') and @class='cdk-overlay-pane']//button[@class='mat-focus-indicator w-100 mat-button-3d mat-button-lg mb-3 mat-flat-button mat-button-base mat-accent ng-star-inserted']")))
    boton_vender1 = AWD.driver1.find_element(
        By.XPATH, "//div[@class='cdk-global-overlay-wrapper' and @style='justify-content: center; align-items: center;']//div[contains(@id,'cdk-overlay-') and @class='cdk-overlay-pane']//button[@class='mat-focus-indicator w-100 mat-button-3d mat-button-lg mb-3 mat-flat-button mat-button-base mat-accent ng-star-inserted']")
    AWD.driver1.execute_script("arguments[0].click();", boton_vender1)

def venta_ventana2():
    AWD.wait1.until(EC.visibility_of_element_located(
        (By.XPATH, "//div[@class='cdk-global-overlay-wrapper' and @style='justify-content: center; align-items: center;']//div[@class='cdk-overlay-pane' and contains(@id,'cdk-overlay-')]//h1[contains(text(),'Send this item')]")))
    vender2 = AWD.driver1.find_element(
        By.XPATH, "//div[@class='cdk-global-overlay-wrapper' and @style='justify-content: center; align-items: center;']//div[@class='cdk-overlay-pane' and contains(@id,'cdk-overlay-')]//h1[contains(text(),'Send this item')]")
    AWD.wait1.until(EC.visibility_of_element_located(
        (By.XPATH, "//span[contains(@class,'text-underline pointer')]")))
    copia_nombre = AWD.driver1.find_element(
        By.XPATH, "//span[contains(@class,'text-underline pointer')]")
    copia_nombre.click()
    time.sleep(2)

    boton_vender2 = AWD.driver1.find_element(
        By.XPATH, "//div[@class='cdk-global-overlay-wrapper' and @style='justify-content: center; align-items: center;']//div[@class='cdk-overlay-pane' and contains(@id,'cdk-overlay-')]//a[contains(@class, 'mat-focus-indicator w-50 mat-button-3d mat-button-lg mat-flat-button mat-button-base mat-accent')]")
    AWD.driver1.execute_script("arguments[0].click();", boton_vender2)

def venta_ventana_tradeo():
    AWD.driver1.switch_to.window(AWD.driver1.window_handles[1])

    AWD.wait1.until(EC.visibility_of_element_located(
        (By.XPATH, "//div[@class='appselect' and @id='appselect']")))
    selector = AWD.driver1.find_element(
        By.XPATH, "//div[@class='appselect' and @id='appselect']")
    AWD.driver1.execute_script("arguments[0].click();", selector)

    AWD.wait1.until(EC.visibility_of_element_located(
        (By.XPATH, "//div[@id='appselect_option_you_730_2']")))
    seleccion = AWD.driver1.find_element(
        By.XPATH, "//div[@id='appselect_option_you_730_2']")
    AWD.driver1.execute_script("arguments[0].click();", seleccion)

    AWD.wait1.until(EC.visibility_of_element_located(
        (By.XPATH, "//input[@class='filter_search_box']")))
    buscar_skin = AWD.driver1.find_element(
        By.XPATH, "//input[@class='filter_search_box']")
    buscar_skin.send_keys(Keys.CONTROL+'v')
    time.sleep(1)

    AWD.wait1.until(EC.visibility_of_element_located(
        (By.XPATH, "//div[@class='itemHolder' and not(@style)]")))
    item = AWD.driver1.find_element(
        By.XPATH, "//div[@class='itemHolder' and not(@style)]//a[@class='inventory_item_link']")
    ActionChains(AWD.driver1).double_click(item).perform()

    AWD.wait1.until(EC.visibility_of_element_located(
        (By.XPATH, "//*[contains(text(),'Click here to confirm trade contents.')]")))
    marcar_pesta = AWD.driver1.find_element(
        By.XPATH, "//*[contains(text(),'Click here to confirm trade contents.')]")
    AWD.driver1.execute_script("arguments[0].click();", marcar_pesta)

    AWD.wait1.until(EC.visibility_of_element_located(
        (By.XPATH, "//div[@class='newmodal']")))
    cuadro_regalo = AWD.driver1.find_element(
        By.XPATH, "//div[@class='newmodal']")
    boton_regalo = cuadro_regalo.find_element(
        By.XPATH, "//div[@class='btn_green_steamui btn_medium']")
    AWD.driver1.execute_script("arguments[0].click();", boton_regalo)

    AWD.wait1.until(EC.visibility_of_element_located(
        (By.XPATH, "//div[@id='trade_confirmbtn']")))
    hacer_oferta = AWD.driver1.find_element(
        By.XPATH, "//div[@id='trade_confirmbtn']")
    AWD.driver1.execute_script("arguments[0].click();", hacer_oferta)

    AWD.wait1.until(EC.visibility_of_element_located(
        (By.XPATH, "//div[@class='newmodal']")))
    cuadro_aceptar = AWD.driver1.find_element(
        By.XPATH, "//div[@class='newmodal']")
    boton_aceptar = cuadro_aceptar.find_element(
        By.XPATH, "//div[@class='btn_grey_steamui btn_medium']")
    AWD.driver1.execute_script("arguments[0].click();", boton_aceptar)

    AWD.driver1.switch_to.window(AWD.driver1.window_handles[0])

    """
    pulsar_detras = driver1.find_element(By.XPATH,"//a[@class='mat-focus-indicator top-up-button mat-button-3d mat-flat-button mat-button-base mat-accent']")
    driver1.execute_script("arguments[0].click();", pulsar_detras)
    """

def cancelar_tradeo():
    tiempo_inicio = time.time()
    while (time.time() - tiempo_inicio) < 480:
        time.sleep(30)
        AWD.driver3.refresh()
        try:
            AWD.driver3.find_element(
                By.XPATH, "//div[@class='tradeoffer_footer_actions']")
        except NoSuchElementException:
            print("La skin se ha vendido.")
            break
    else:
        tradeo_enviado = AWD.driver3.find_element(
            By.XPATH, "//div[@class='tradeoffer_footer_actions']")
        tradeo_enviado.click()
        AWD.wait3.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='newmodal']")))
        cuadro_cancelar_tradeo = AWD.driver3.find_element(
            By.XPATH, "//div[@class='newmodal']//div[@class='btn_green_steamui btn_medium']")
        cuadro_cancelar_tradeo.click()
        AWD.driver3.refresh()
    #Añadir aqui intrucciones para volver a la pestaña de venta y tal.

"""
def cancelar_tradeo2():
    tiempo_inicio = time.time()
    trade_offer_ID=#sacar el ID de la oferta de tradeo
    url=f"https://steamcommunity.com/tradeoffer/{trade_offer_ID}}/"
    while (time.time() - tiempo_inicio) < 480:
        driver.execute_script("window.open('');")

        # Cambia al nuevo tab (pestaña)
        driver.switch_to.window(driver.window_handles[1])

        # Carga una URL en la nueva pestaña
        driver.get("https://www.bing.com")
"""