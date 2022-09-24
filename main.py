import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  #..............
from selenium.webdriver.support import expected_conditions as EC    #................
from bs4 import BeautifulSoup
import xlsxwriter
import time
# from selenium.webdriver.common.proxy import Proxy, ProxyType  #.................
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from msvcrt import getche, getch
import os

def gen_driver(self):
    chrome_options = uc.ChromeOptions()
    chrome_options.headless = True
    chrome_options.add_argument('--proxy-server=http://'+PROXY)
    driver = uc.Chrome(options=chrome_options)
    return driver
