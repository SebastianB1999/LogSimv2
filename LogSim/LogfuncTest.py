import unittest
from Logfunc import AndGate
from Logfunc import OrGate
from Logfunc import NandGate
from Logfunc import XORGate



class AndGateTest(unittest.TestCase):
    def testcase_00(self):
        a = AndGate(2)
        self.assertEqual(False, a.Output, "Class OrGate Testcase 0 failed.")

    def testcase_01(self):
        a = AndGate(2)
        a.set_input(0,False)
        a.set_input(1,False)
        a.execute()
        self.assertEqual(False, a.Output, "Class AndGate Testcase 1 failed.")

    def testcase_02(self):
        a = AndGate(2)
        a.set_input(0,False)
        a.set_input(1,True)
        a.execute()
        self.assertEqual(False, a.Output, "Class AndGate Testcase 2 failed.")

    def testcase_03(self):
        a = AndGate(2)
        a.set_input(0,True)
        a.set_input(1,False)
        a.execute()
        self.assertEqual(False, a.Output, "Class AndGate Testcase 3 failed.")

    def testcase_04(self):
        a = AndGate(2)
        a.set_input(0,True)
        a.set_input(1,True)
        a.execute()
        self.assertEqual(True, a.Output, "Class AndGate Testcase 4 failed.")


class OrGateTest(unittest.TestCase):
    def testcase_00(self):
        a = OrGate(2)
        self.assertEqual(False, a.Output, "Class OrGate Testcase 0 failed.")

    def testcase_01(self):
        a = OrGate(2)
        a.set_input(0,False)
        a.set_input(1,False)
        a.execute()
        self.assertEqual(False, a.Output, "Class OrGate Testcase 1 failed.")

    def testcase_02(self):
        a = OrGate(2)
        a.set_input(0,False)
        a.set_input(1,True)
        a.execute()
        self.assertEqual(True, a.Output, "Class OrGate Testcase 2 failed.")

    def testcase_03(self):
        a = OrGate(2)
        a.set_input(0,True)
        a.set_input(1,False)
        a.execute()
        self.assertEqual(True, a.Output, "Class OrGate Testcase 3 failed.")

    def testcase_04(self):
        a = OrGate(2)
        a.set_input(0,True)
        a.set_input(1,True)
        a.execute()
        self.assertEqual(True, a.Output, "Class OrGate Testcase 4 failed.")

class NandGateTest(unittest.TestCase):
    def testcase_00(self):
        a = NandGate(2)
        self.assertEqual(True, a.Output, "Class OrGate Testcase 0 failed.")

    def testcase_01(self):
        a = NandGate(2)
        a.set_input(0,False)
        a.set_input(1,False)
        a.execute()
        self.assertEqual(True, a.Output, "Class OrGate Testcase 1 failed.")

    def testcase_02(self):
        a = NandGate(2)
        a.set_input(0,False)
        a.set_input(1,True)
        a.execute()
        self.assertEqual(False, a.Output, "Class OrGate Testcase 2 failed.")

    def testcase_03(self):
        a = NandGate(2)
        a.set_input(0,True)
        a.set_input(1,False)
        a.execute()
        self.assertEqual(False, a.Output, "Class OrGate Testcase 3 failed.")

    def testcase_04(self):
        a = NandGate(2)
        a.set_input(0,True)
        a.set_input(1,True)
        a.execute()
        self.assertEqual(False, a.Output, "Class OrGate Testcase 4 failed.")

class XORGateTest(unittest.TestCase):
    
    def testcase_00(self):
        a = XORGate(2)
        self.assertEqual(False, a.Output, "Class OrGate Testcase 0 failed.")

    def testcase_01(self):
        a = XORGate(2)
        a.set_input(0,False)
        a.set_input(1,False)
        a.execute()
        self.assertEqual(False, a.Output, "Class OrGate Testcase 1 failed.")

    def testcase_02(self):
        a = XORGate(2)
        a.set_input(0,False)
        a.set_input(1,True)
        a.execute()
        self.assertEqual(True, a.Output, "Class OrGate Testcase 2 failed.")

    def testcase_03(self):
        a = XORGate(2)
        a.set_input(0,True)
        a.set_input(1,False)
        a.execute()
        self.assertEqual(True, a.Output, "Class OrGate Testcase 3 failed.")

    def testcase_04(self):
        a = XORGate(2)
        a.set_input(0,True)
        a.set_input(1,True)
        a.execute()
        self.assertEqual(False, a.Output, "Class OrGate Testcase 4 failed.")



if __name__ == "__main__":
    unittest.main()