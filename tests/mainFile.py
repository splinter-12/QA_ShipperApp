import LoginTestFile
import ForgotPassTestFile
import createAccountTests
import unittest
from HtmlTemplate import Report
import time
class ShipperAppClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report= Report()
        cls.report.WriteReportHeader()

    def test_bloc_1(self):
        seconds = time.time()
        local_time = time.ctime(seconds)
        try:
            suite = unittest.TestLoader().loadTestsFromModule(LoginTestFile)
            unittest.TextTestRunner(verbosity=2).run(suite)
            self.report.appendToReport("1",'Login page tests',local_time , "passed")
        except Exception:
            self.report.appendToReport("1",'Login page tests',local_time , "failed")

    def test_bloc_2(self):
        seconds = time.time()
        local_time = time.ctime(seconds)
        try:
            suite = unittest.TestLoader().loadTestsFromModule(ForgotPassTestFile)
            unittest.TextTestRunner(verbosity=2).run(suite)
            self.report.appendToReport("2",'Forgot password tests',local_time , "passed")
        except Exception:
            self.report.appendToReport("2",'Forgot password tets',local_time , "failed")

    def test_bolc_3(self):
        seconds = time.time()
        local_time = time.ctime(seconds)
        try:
            suite = unittest.TestLoader().loadTestsFromModule(createAccountTests)
            unittest.TextTestRunner(verbosity=2).run(suite)
            self.report.appendToReport("3",'Registration p1',local_time , "passed")
        except Exception:
            self.report.appendToReport("3",'Registration p1',local_time , "failed")
    @classmethod
    def tearDownClass(cls):
        cls.report.writeReportFooter()
        cls.report.writeToFile('FinalReport.html')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(ShipperAppClass('test_bloc_1'))
    suite.addTest(ShipperAppClass('test_bloc_2'))
    suite.addTest(ShipperAppClass('test_bolc_3'))
    runner = unittest.TextTestRunner()
    runner.run(suite)




















