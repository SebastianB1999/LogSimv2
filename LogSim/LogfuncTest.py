import unittest
from Logfunc import AndGate
from Logfunc import OrGate
from Logfunc import NandGate
from Logfunc import XORGate



class AndGateTest(unittest.TestCase):
    def testcase_00(self):
        a = AndGate()
        self.assertEqual(False, a.Output, "Class OrGate Testcase 0 failed.")

    def testcase_01(self):
        a = AndGate()
        a.Input = False
        a.Input = False
        a.execute()
        self.assertEqual(False, a.Output, "Class AndGate Testcase 1 failed.")

    def testcase_02(self):
        a = AndGate()
        a.Input = False
        a.Input = True
        a.execute()
        self.assertEqual(False, a.Output, "Class AndGate Testcase 2 failed.")

    def testcase_03(self):
        a = AndGate()
        a.Input = True
        a.Input = False
        a.execute()
        self.assertEqual(False, a.Output, "Class AndGate Testcase 3 failed.")

    def testcase_04(self):
        a = AndGate()
        a.Input = True
        a.Input = True
        a.execute()
        self.assertEqual(True, a.Output, "Class AndGate Testcase 4 failed.")


class OrGateTest(unittest.TestCase):
    def testcase_00(self):
        a = OrGate()
        self.assertEqual(False, a.Output, "Class OrGate Testcase 0 failed.")

    def testcase_01(self):
        a = OrGate()
        a.Input = False
        a.Input = False
        a.execute()
        self.assertEqual(False, a.Output, "Class OrGate Testcase 1 failed.")

    def testcase_02(self):
        a = OrGate()
        a.Input = False
        a.Input = True
        a.execute()
        self.assertEqual(True, a.Output, "Class OrGate Testcase 2 failed.")

    def testcase_03(self):
        a = OrGate()
        a.Input = True
        a.Input = False
        a.execute()
        self.assertEqual(True, a.Output, "Class OrGate Testcase 3 failed.")

    def testcase_04(self):
        a = OrGate()
        a.Input = True
        a.Input = True
        a.execute()
        self.assertEqual(True, a.Output, "Class OrGate Testcase 4 failed.")

class NandGateTest(unittest.TestCase):
    def testcase_00(self):
        a = NandGate()
        self.assertEqual(True, a.Output, "Class OrGate Testcase 0 failed.")

    def testcase_01(self):
        a = NandGate()
        a.Input = False
        a.Input = False
        a.execute()
        self.assertEqual(True, a.Output, "Class OrGate Testcase 1 failed.")

    def testcase_02(self):
        a = NandGate()
        a.Input = False
        a.Input = True
        a.execute()
        self.assertEqual(False, a.Output, "Class OrGate Testcase 2 failed.")

    def testcase_03(self):
        a = NandGate()
        a.Input = True
        a.Input = False
        a.execute()
        self.assertEqual(False, a.Output, "Class OrGate Testcase 3 failed.")

    def testcase_04(self):
        a = NandGate()
        a.Input = True
        a.Input = True
        a.execute()
        self.assertEqual(False, a.Output, "Class OrGate Testcase 4 failed.")

class XORGateTest(unittest.TestCase):
    
    def testcase_00(self):
        a = XORGate()
        self.assertEqual(False, a.Output, "Class OrGate Testcase 0 failed.")

    def testcase_01(self):
        a = XORGate()
        a.Input = False
        a.Input = False
        a.execute()
        self.assertEqual(False, a.Output, "Class OrGate Testcase 1 failed.")

    def testcase_02(self):
        a = XORGate()
        a.Input = False
        a.Input = True
        a.execute()
        self.assertEqual(True, a.Output, "Class OrGate Testcase 2 failed.")

    def testcase_03(self):
        a = XORGate()
        a.Input = True
        a.Input = False
        a.execute()
        self.assertEqual(True, a.Output, "Class OrGate Testcase 3 failed.")

    def testcase_04(self):
        a = XORGate()
        a.Input = True
        a.Input = True
        a.execute()
        self.assertEqual(False, a.Output, "Class OrGate Testcase 4 failed.")



if __name__ == "__main__":
    unittest.main()