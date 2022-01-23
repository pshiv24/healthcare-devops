from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import unittest
import HtmlTestRunner

class HomePageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/usr/local/bin/chromedriver")
        self.driver.get("http://13.59.2.216")
        self.driver.maximize_window()
        time.sleep(4)

    def testPythonScript(self):
        chromedriver=self.driver
        chromedriver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(2)
        patientimage=chromedriver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/div/a[2]/div/img')
        patientimage.click()
        time.sleep(5)

        chromedriver.back()
       
        doctorimage=chromedriver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/div/a[1]/div/img')
        doctorimage.click()
        time.sleep(3)

        about=chromedriver.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div/a[1]')
        about.click()
        time.sleep(5)
        

        appintment=chromedriver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div/div/a[2]')
        appintment.click()
        time.sleep(5)
        chromedriver.back()

        doctor=chromedriver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div/div/a[4]')
        doctor.click()
        time.sleep(5)
        chromedriver.back()

        patient=chromedriver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div/div/a[3]')
        patient.click()
        time.sleep(5)
        chromedriver.back()

        


    def test_fail(self):
        driver=self.driver
        addPatient=driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[4]/form/div/button')
        addPatient.click()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))
