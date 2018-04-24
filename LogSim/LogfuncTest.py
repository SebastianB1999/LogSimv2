import unittest
from Logfunc import AndGate
from Logfunc import OrGate


class AndGateTest(unittest.TestCase):
    def testcase_01(self):
        a = AndGate()
        a.Input0 = False
        a.Input1 = False
        a.execute()
        self.assertEqual(False, a.Output, "Class AndGate Testcase 1 failed.")

    def testcase_02(self):
        a = AndGate()
        a.Input0 = False
        a.Input1 = True
        a.execute()
        self.assertEqual(False, a.Output, "Class AndGate Testcase 2 failed.")

    def testcase_03(self):
        a = AndGate()
        a.Input0 = True
        a.Input1 = False
        a.execute()
        self.assertEqual(False, a.Output, "Class AndGate Testcase 3 failed.")

    def testcase_04(self):
        a = AndGate()
        a.Input0 = True
        a.Input1 = True
        a.execute()
        self.assertEqual(True, a.Output, "Class AndGate Testcase 4 failed.")


class OrGateTest(unittest.TestCase):
    def testcase_01(self):
        a = OrGate()
        a.Input0 = False
        a.Input1 = False
        a.execute()
        self.assertEqual(False, a.Output, "Class OrGate Testcase 1 failed.")

    def testcase_02(self):
        a = OrGate()
        a.Input0 = False
        a.Input1 = True
        a.execute()
        self.assertEqual(True, a.Output, "Class OrGate Testcase 2 failed.")

    def testcase_03(self):
        a = OrGate()
        a.Input0 = True
        a.Input1 = False
        a.execute()
        self.assertEqual(True, a.Output, "Class OrGate Testcase 3 failed.")

    def testcase_04(self):
        a = OrGate()
        a.Input0 = True
        a.Input1 = True
        a.execute()
        self.assertEqual(True, a.Output, "Class OrGate Testcase 4 failed.")



if __name__ == "__main__":
    unittest.main()