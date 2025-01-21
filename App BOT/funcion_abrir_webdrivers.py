import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

driver1=None
driver3=None
driver4=None
wait1 = WebDriverWait(driver1, 600)
wait3 = WebDriverWait(driver3, 1000000000)
wait4 = WebDriverWait(driver4, 1000000000)

def abrir_webdrivers():
    global driver1, driver3, driver4, wait1, wait3
    options = Options()
    options.add_argument("--disable-popup-blocking")
    driver1 = uc.Chrome(options=options)
    driver1.maximize_window()
    driver1.get("https://www.csgoroll.com/en/top-up/steam/csgo")
    driver3 = uc.Chrome()
    driver3.get("https://steamcommunity.com/id/WiTe98/tradeoffers/sent/")
    driver3.maximize_window()
    driver4 = uc.Chrome()
    driver4.maximize_window()

def cerrar_webdrivers():
    global driver1,driver3
    driver1.quit()
    driver3.quit()
    driver4.quit()