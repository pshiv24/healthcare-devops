from selenium import webdriver
import time
import unittest
import HtmlTestRunner 
from selenium.webdriver.common.keys import Keys


class PatientLoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/usr/local/bin/chromedriver")
        self.driver.get("http://13.59.2.216")
        self.driver.maximize_window()
        time.sleep(4)
        
    def testPythonScript(self):
        driver=self.driver

        patient_portal = driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/a[3]")
        patient_portal.click()

        patient_id = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div/div/div/div/form/div/div[1]/div/div/input")
        patient_id.send_keys("1")

        patient_sk = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div/div/div/div/form/div/div[2]/div/div/input")
        patient_sk.send_keys("1234")

        patient_btn = driver.find_element_by_xpath('//*[@id="contact-form"]/div/div[3]/center/div/div/button[1]')
        patient_btn.click()

        time.sleep(5)

        driver.back()
        time.sleep(5)

        patient_id = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div/div/div/div/form/div/div[1]/div/div/input")
        patient_id.send_keys("1")

        patient_sk = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div/div/div/div/form/div/div[2]/div/div/input")
        patient_sk.send_keys("1234")
        driver.execute_script("window.scrollTo(0,0);")
        time.sleep(2)
        patient_btn2 = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div/div/div/div/form/div/div[3]/center/div/div/button[2]")
        patient_btn2.click()
        time.sleep(5)

    def test_fail(self):
        driver=self.driver
        addPatient=driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[4]/form/div/button')
        addPatient.click()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))