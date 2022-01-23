from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import unittest
import HtmlTestRunner

class DoctorDashboardTest(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome("/usr/local/bin/chromedriver")
        self.driver.get("http://13.59.2.216")
        self.driver.maximize_window()
        time.sleep(4)

    def testPythonScript(self):
        driver=self.driver

        doctorPortal=driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div/div/a[4]')
        doctorPortal.click()

        email=driver.find_element_by_id("form_d_email")
        email.send_keys("pshivangi1999@gmail.com")
        email.send_keys(Keys.RETURN)

        passwd=driver.find_element_by_xpath('//*[@id="form_d_pass"]')
        passwd.send_keys("admin@123")
        passwd.send_keys(Keys.RETURN)

        login=driver.find_element_by_xpath('//*[@id="contact-form"]/div/div[3]/center/div/div/button')
        login.click()
        time.sleep(2)

        # logout=driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[2]/div/div/form/button')
        # logout.click()
        # time.sleep(2)
        # driver.back()

        driver.maximize_window()
        time.sleep(4)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(2)

        addPrescription=driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[3]/form/div/button')
        addPrescription.click()
        time.sleep(2)
        driver.back()

        addPatient=driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[4]/form/div/button')
        addPatient.click()
        time.sleep(2)
        driver.back()

    def test_fail(self):
        driver=self.driver
        addPatient=driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[4]/form/div/button')
        addPatient.click()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))
