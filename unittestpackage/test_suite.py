import unittest
from unittestpackage.test1 import Test
from unittestpackage.test_assertion import TestAssertion

#  get all test functions from Test and TestAssertion
tc1 = unittest.TestLoader().loadTestsFromTestCase(Test)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestAssertion)

#  Create a Test Suite combining Test and TestAssertion
smoke_test = unittest.TestSuite([tc1, tc2])
unittest.TextTestRunner().run(smoke_test)