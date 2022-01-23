import unittest
import patientLoginTest
import makeAppointmentTest as makeAppointmentTest
import homepageTest as homePageTest
import doctorLoginTest as doctorLoginTest
import doctorDashboardTest as doctorDashboardTest
import addPatientTest as addPatientTest
import addPrescriptionTest as addPrescriptionTest
import os
 
# Import the HTMLTestRunner Module
import HtmlTestRunner
 
# Get the Present Working Directory since that is the place where the report
# would be stored
 
current_directory = os.getcwd()
 
class HTML_TestRunner_TestSuite(unittest.TestCase):
    def test_GoogleWiki_Search(self):
 
        # Create a TestSuite comprising the two test cases
        consolidated_test = unittest.TestSuite()
 
        # Add the test cases to the Test Suite
        consolidated_test.addTests([
            #unittest.defaultTestLoader.loadTestsFromTestCase(seleniumTest.LoginTest),
            #unittest.defaultTestLoader.loadTestsFromTestCase(test2.AnotherTest),
            unittest.defaultTestLoader.loadTestsFromTestCase(homePageTest.HomePageTest),
            unittest.defaultTestLoader.loadTestsFromTestCase(makeAppointmentTest.MakeAppointmentTest),
            unittest.defaultTestLoader.loadTestsFromTestCase(doctorLoginTest.DoctorLoginTest),
            unittest.defaultTestLoader.loadTestsFromTestCase(doctorDashboardTest.DoctorDashboardTest),
            unittest.defaultTestLoader.loadTestsFromTestCase(addPatientTest.AddPatientTest),
            unittest.defaultTestLoader.loadTestsFromTestCase(addPrescriptionTest.AddPrescriptionTest),
            unittest.defaultTestLoader.loadTestsFromTestCase(patientLoginTest.PatientLoginTest)
        ])
 
        output_file = open(current_directory + "\HTML_Test_Runner_ReportTest.html", "w")
 
        html_runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            stream=output_file,
            report_title='HTML Reporting using PyUnit',
            descriptions='HTML Reporting using PyUnit & HTMLTestRunner'
        )
 
        html_runner.run(consolidated_test)
 
if __name__ == '__main__':
    unittest.main()