from socket import if_nameindex
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  #..............
from selenium.webdriver.support import expected_conditions as EC    #................
# from bs4 import BeautifulSoup
# import xlsxwriter
# import time
# from selenium.webdriver.common.proxy import Proxy, ProxyType  #.................
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from msvcrt import getche, getch
import os

# url = "https://www.google.com/search?as_st=y&tbm=isch&as_q=&as_epq=badshahi+mosque&as_oq=&as_eq=&cr=&as_sitesearch=&safe=images&tbs=isz:lt,islt:xga"

def gen_driver(self):
    chrome_options = uc.ChromeOptions()
    chrome_options.headless = True
    # chrome_options.add_argument('--proxy-server=http://'+PROXY)
    driver = uc.Chrome(options=chrome_options)
    return driver

 
if __name__ == "__main__":
    print ("Executed when invoked directly")
else:
    print ("Executed when imported")
# 