from selenium.webdriver.common.by import By

#~-- MIS IMPORTACIONES --~#
import funcion_abrir_webdrivers as AWD
#~-- MIS IMPORTACIONES --~#

"""
class TradeNotConfirmed:
    def __init__(self):
"""        

def trade_not_confirmed():
    cuadro_trade_not_confirmed = AWD.driver1.find_element(By.XPATH,"//div[@class='cdk-overlay-pane' and contains(@id,'cdk-overlay')]//mat-dialog-container[contains(@id,'mat-dialog-')]//h1[contains(text(),'Trade Not Confirmed')]")
    boton_cuadro_trade_not_confirmed = cuadro_trade_not_confirmed.find_element(By.XPATH,"//button[@class='mat-focus-indicator w-100 mat-button-3d mat-button-lg mat-flat-button mat-button-base mat-warn']")
    AWD.driver1.execute_script("arguments[0].click();", boton_cuadro_trade_not_confirmed)

def warning():
    cuadro_warning = AWD.driver1.find_element(By.XPATH,"//div[@class='cdk-overlay-pane' and contains(@id,'cdk-overlay')]//mat-dialog-container[contains(@id,'mat-dialog-')]//h1[contains(text(),'Warning!')]")
    boton_cuadro_warning1 = cuadro_warning.find_element(By.XPATH,"//mat-checkbox[@class='mat-checkbox mb-3 mat-primary ng-valid ng-dirty ng-touched']")
    AWD.driver1.execute_script("arguments[0].click();", boton_cuadro_warning1)
    boton_cuadro_Warning2 = cuadro_warning.find_element(By.XPATH,"//button[@class='mat-focus-indicator w-100 mat-button-3d mat-button-lg mat-flat-button mat-button-base mat-warn']")
    AWD.driver1.execute_script("arguments[0].click();", boton_cuadro_Warning2)

def waiting():
    cuadro_waiting = AWD.driver1.find_element(By.XPATH,"//div[@class='cdk-overlay-pane' and contains(@id,'cdk-overlay')]//mat-dialog-container[contains(@id,'mat-dialog-')]//h1[contains(text(),'Waiting')]")
    boton_cuadro_waiting = AWD.driver1.find_element(By.XPATH,"//button[@class='mat-focus-indicator w-100 mat-button-3d mat-button-lg mat-flat-button mat-button-base mat-accent']")

def trade_complete_con_foto():
    cuadro_trade_complete = AWD.driver1.find_element(By.XPATH,"//div[@class='cdk-overlay-pane' and contains(@id,'cdk-overlay')]//mat-dialog-container[contains(@id,'mat-dialog-')]//h1[contains(text(),'Trade Complete')]")
    boton_cuadro_trade_complete = cuadro_trade_complete.find_element(By.XPATH,"//button[@class='mat-focus-indicator w-100 mat-button-3d mat-button-lg mt-3 mat-flat-button mat-button-base mat-accent']")

def trade_complete_sin_foto():
    cuadro_trade_complete2 = AWD.driver1.find_element(By.XPATH,"//div[@class='cdk-overlay-pane' and contains(@id,'cdk-overlay')]//mat-dialog-container[contains(@id,'mat-dialog-')]//h1[contains(text(),'Trade Complete')]")
    boton_cuadro_trade_complete2 = cuadro_trade_complete2.find_element(By.XPATH,"//button[@class='mat-focus-indicator w-100 mat-button-3d mat-button-lg mat-flat-button mat-button-base mat-accent']")