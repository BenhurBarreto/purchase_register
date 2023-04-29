from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class ConsultaNF:

    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.driver.get(url)

    def coleta_dados_da_NF(self):
        time.sleep(2)
        self.driver.close()
