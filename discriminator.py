from itertools import count
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  #..............
from selenium.webdriver.support import expected_conditions as EC    #................
import requests # to get image from the web
import shutil # to save it locally
from urllib.parse import urlparse
# from bs4 import BeautifulSoup
# import xlsxwriter
import time
# from selenium.webdriver.common.proxy import Proxy, ProxyType  #.................
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from msvcrt import getche, getch
import os

# url = "https://www.google.com/search?as_st=y&tbm=isch&as_q=&as_epq=badshahi+mosque&as_oq=&as_eq=&cr=&as_sitesearch=&safe=images&tbs=isz:lt,islt:xga"

def gen_driver():
    chrome_options = uc.ChromeOptions()
    # chrome_options.headless = True
    # chrome_options.add_argument('--proxy-server=http://'+PROXY)
    driver = uc.Chrome(options=chrome_options)
    return driver


class Governor:
    def __init__(self):
        self.driver = gen_driver()
        self.images_list = os.listdir(os.getcwd()+ r"\Photoshoped_images")
        self.pre_image_path = os.getcwd() + "\\Photoshoped_images\\"

        self.initiate()
        for i, img in enumerate(self.images_list, 1):
            image_path = self.pre_image_path + img
            self.search_img(i, image_path)
            # input()

    def initiate(self):
        self.driver.get("https://tineye.com/")


    def search_img(self, index, image_path):
        self.driver.find_element(By.XPATH, '//*[@id="upload_box"]').send_keys(image_path)
        time.sleep(6)
        print("[{}] Matching results found: {}".format(index,self.count_matches()))

    def count_matches(self):
        result = ""
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="result_count"]')))
            result = self.driver.find_element(By.XPATH, '//*[@id="result_count"]').text
        except:
            # result = self.driver.find_element(By.XPATH, '//*[@id="result_count"]').text
            result = "0 matches found"
        return result
        

 
if __name__ == "__main__":
    agency = Governor()
    # driver = gen_driver()
    # driver.get("https://tineye.com/")
    # # driver.findElement(By.id("inputFile")).sendKeys("C:/path/to/file.jpg");
    # images_list = os.listdir(os.getcwd()+ r"\Photoshoped_images")
    # image_path = os.getcwd() + "\\Photoshoped_images\\" + images_list[1]
    # print(image_path)
    # driver.find_element(By.XPATH, '//*[@id="upload_box"]').send_keys(image_path)
    # input()