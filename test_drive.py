from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver 
import time
import math
import unittest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class testDrive(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

    def test_testdrive_form_send(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://qa.bmw.kodixauto.ru/all-forms/")
        assert "Формы" in driver.title

        self = driver.find_element_by_xpath('//*[@id="test_drive_form"]/div/div[1]/div[2]/div[1]/div/div/div/div[1]')
        self.send_keys(Keys.ENTER)
        time.sleep(1)
        self.send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        self.send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        self.send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        self.send_keys(Keys.ENTER)
        time.sleep(2)

    
        self = driver.find_element_by_xpath('//*[@id="test_drive_form"]/div/div[1]/div[2]/div[2]/div/div[1]/label')
        self.send_keys('20092019')
        time.sleep(1)

        self = driver.find_element_by_xpath('//*[@id="test_drive_form"]/div/div[1]/div[2]/div[3]/div/div[1]/label')
        self.click()
        self.send_keys('1231')
        time.sleep(0.5)

        self = driver.find_element_by_xpath('//*[@id="test_drive_form"]/div/div[2]/div/div/div/div/div/div[1]')
        self.click()
        self.send_keys(Keys.ENTER)
        time.sleep(0.5)
        self.send_keys(Keys.ARROW_DOWN)
        time.sleep(0.5)
        self.send_keys(Keys.ARROW_DOWN)
        time.sleep(0.5)
        self.send_keys(Keys.ENTER)
        time.sleep(0.5)

        self = driver.find_element_by_xpath('//*[@id="test_drive_form"]/div/div[3]/div[2]/div[1]/div/div/label[2]/div/span[1]')
        self.click()
        time.sleep(0.5)

        self = driver.find_element_by_xpath('/html/body/div[1]/main/div[3]/div/div[2]/div/div/div/div/div/div/div[2]/form/div/div[3]/div[2]/div[2]/div/div[1]/label/input')
        self.send_keys('Андрей')
        time.sleep(0.5)

        self = driver.find_element_by_xpath('/html/body/div[1]/main/div[3]/div/div[2]/div/div/div/div/div/div/div[2]/form/div/div[3]/div[2]/div[3]/div/div/label/input')
        self.send_keys('Иванов')
        time.sleep(0.5)

        self = driver.find_element_by_xpath('/html/body/div[1]/main/div[3]/div/div[2]/div/div/div/div/div/div/div[2]/form/div/div[4]/div[2]/div[1]/div/div[1]/label/input')
        self.send_keys(Keys.ENTER)
        time.sleep(1)
        self.send_keys(Keys.ARROW_LEFT)
        self.send_keys(Keys.ARROW_LEFT)
        self.send_keys(Keys.ARROW_LEFT)
        self.send_keys(Keys.ARROW_LEFT)
        self.send_keys(Keys.ARROW_LEFT)
        self.send_keys(Keys.ARROW_LEFT)
        self.send_keys(Keys.ARROW_LEFT)
        self.send_keys(Keys.ARROW_LEFT)
        self.send_keys(Keys.ARROW_LEFT)
        self.send_keys(Keys.ARROW_LEFT)
        self.send_keys(Keys.ARROW_LEFT)
        self.send_keys(Keys.ARROW_LEFT)
        self.send_keys(Keys.ARROW_LEFT)
        self.send_keys(Keys.ARROW_LEFT)
        self.send_keys('9991234567')
        self.send_keys(Keys.ENTER)
        time.sleep(0.5)

        self = driver.find_element_by_xpath('/html/body/div[1]/main/div[3]/div/div[2]/div/div/div/div/div/div/div[2]/form/div/div[4]/div[2]/div[2]/div/div[1]/label/input')
        self.send_keys('ana@kodix.ru')
        time.sleep(1)

        self = driver.find_element_by_xpath('/html/body/div[1]/main/div[3]/div/div[2]/div/div/div/div/div/div/div[2]/form/div/div[5]/div[2]/div/div/div/label/textarea')
        self.send_keys('Vivamus magna justo, lacinia eget consectetur sed, convallis at tellus. Mauris blandit aliquet elit, eget tincidunt nibh pulvinar a. Vivamus magna justo, lacinia eget consectetur sed, convallis at tellus. Nulla porttitor accumsan tincidunt. Nulla porttitor accumsan tincidunt. Vivamus magna justo, lacinia eget consectetur sed, convallis at tellus.')

        self = driver.find_element_by_xpath('/html/body/div[1]/main/div[3]/div/div[2]/div/div/div/div/div/div/div[2]/form/div/div[6]/div/div/div/div[1]/label/input')
        self.click()
        time.sleep(1)

        self = driver.find_element_by_xpath('/html/body/div[1]/main/div[3]/div/div[2]/div/div/div/div/div/div/div[2]/form/div/div[7]/div/button')
        self.click()
        time.sleep(10)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
	unittest.main()