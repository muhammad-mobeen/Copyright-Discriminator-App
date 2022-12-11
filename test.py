import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  #..............
from selenium.webdriver.support import expected_conditions as EC

def gen_driver():
    try:
        chrome_options = uc.ChromeOptions()
        # chrome_options.headless = True
        # chrome_options.add_argument('--proxy-server=http://'+PROXY)
        driver = uc.Chrome(options=chrome_options)
        return driver
    except Exception as e:
        print("Error in Driver: ",e)

driver = gen_driver()
driver.get("https://play.google.com/store/games")
input()
driver.get("")