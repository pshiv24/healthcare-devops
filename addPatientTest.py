from select import select
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import unittest
import HtmlTestRunner

class AddPatientTest(unittest.TestCase):

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

        driver.maximize_window()
        time.sleep(4)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(4)

        addPatient=driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[4]/form/div/button')
        addPatient.click()
        time.sleep(2)

        firstname=driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[2]/div/div/div/div/form/div/div[1]/div[1]/div/input')
        firstname.send_keys("Shivangi")
        time.sleep(2)
        #firstname.send_keys(Keys.RETURN)

        last_name = driver.find_element_by_xpath('//*[@id="form_p_lname"]')
        last_name.send_keys("P")
        last_name.send_keys(Keys.RETURN)
        time.sleep(2)
        dob = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div/div/div/div/form/div/div[2]/div[1]/div/input")
        dob.send_keys("07/01/2022")
        dob.send_keys(Keys.RETURN)
        time.sleep(2)
        email = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div/div/div/div/form/div/div[2]/div[2]/div/input")
        email.send_keys("patient@gmail.com")
        email.send_keys(Keys.RETURN)
        gender = Select(driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div/div/div/div/form/div/div[3]/div[1]/div/select"))
        gender.select_by_index('2')
        time.sleep(2)
        mobile = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div/div/div/div/form/div/div[3]/div[2]/div/input")
        mobile.send_keys("77777777")
        mobile.send_keys(Keys.RETURN)
        time.sleep(2)
        height = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div/div/div/div/form/div/div[4]/div[1]/div/input")
        height.send_keys("155")
        height.send_keys(Keys.RETURN)
        time.sleep(2)
        weight = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div/div/div/div/form/div/div[4]/div[2]/div/input")
        weight.send_keys("55")
        weight.send_keys(Keys.RETURN)
        time.sleep(2)
        secret_key = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div/div/div/div/form/div/div[5]/div/div/input")
        secret_key.send_keys("1234")
        secret_key.send_keys(Keys.RETURN)
        time.sleep(2)
        address = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div/div/div/div/form/div/div[6]/div/div/textarea")
        address.send_keys("Delhi")
        address.send_keys(Keys.RETURN)
        time.sleep(2)

        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(2)
        patient_add_btn = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div/div/div/div/form/div/div[7]/center/div/div/button")
        patient_add_btn.click()
        time.sleep(2)

    def test_fail(self):
        driver=self.driver
        addPatient=driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[4]/form/div/button')
        addPatient.click()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))