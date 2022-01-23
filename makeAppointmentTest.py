from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import unittest
import HtmlTestRunner

class MakeAppointmentTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/usr/local/bin/chromedriver")
        self.driver.get("http://13.59.2.216")
        self.driver.maximize_window()
        time.sleep(4)

    def testPythonScript(self):
        chromedriver=self.driver

        appointment=chromedriver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div/div/a[2]')
        appointment.click()
        time.sleep(5)

        #Appointment Part
        drop=Select(chromedriver.find_element_by_xpath('//*[@id="form_doctor"]'))
        drop.select_by_index(3)
        time.sleep(5)

        date=chromedriver.find_element_by_xpath('//*[@id="form_date"]')
        date.click()
        time.sleep(5)

        firstname=chromedriver.find_element_by_xpath('//*[@id="form_p_fname"]')
        firstname.send_keys('Rachna')
        time.sleep(5)

        lastname=chromedriver.find_element_by_xpath('//*[@id="form_p_lname"]')
        lastname.send_keys('kumari')
        time.sleep(5)
        appointmentTime=Select(chromedriver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[2]/div/div/div/div/form/div/div[3]/div[1]/div/select'))
        appointmentTime.select_by_index(0)
        time.sleep(5)

        phone=chromedriver.find_element_by_xpath('//*[@id="form_p_mob_no"]')
        phone.send_keys('76467')
        time.sleep(5)


        issue=chromedriver.find_element_by_xpath('//*[@id="form_p_issue"]')
        issue.send_keys("fever and back pain")
        time.sleep(5)

        checkbox=chromedriver.find_element_by_xpath('//*[@id="form_exist"]')
        checkbox.click()
        time.sleep(5)

        chromedriver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(2)
        makeappointment=chromedriver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[2]/div/div/div/div/form/div/div[5]/center/div/div/button')
        makeappointment.click()
        time.sleep(5)

    def test_fail(self):
        driver=self.driver
        addPatient=driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[4]/form/div/button')
        addPatient.click()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))