import unittest
from Logfunc import AndGate
from Logfunc import OrGate
from Logfunc import NandGate
from Logfunc import XORGate
from Logfunc import NorGate


class AndGateTest(unittest.TestCase):
    def testcase_00(self):
        a = AndGate(2)
        self.assertEqual(False, a.Output[0], "Class AndGate Testcase 0 failed.")
        self.assertEqual(False, a.Input[0], "Class AndGate Testcase 0 failed.")
        self.assertEqual(False, a.Input[1], "Class AndGate Testcase 0 failed.")

    def testcase_01(self):
        a = AndGate(2)
        a.set_input(0,False)
        a.set_input(1,False)
        a.execute()
        self.assertEqual(False, a.Output[0], "Class AndGate Testcase 1 failed.")

    def testcase_02(self):
        a = AndGate(2)
        a.set_input(0,False)
        a.set_input(1,True)
        a.execute()
        self.assertEqual(False, a.Output[0], "Class AndGate Testcase 2 failed.")

    def testcase_03(self):
        a = AndGate(2)
        a.set_input(0,True)
        a.set_input(1,False)
        a.execute()
        self.assertEqual(False, a.Output[0], "Class AndGate Testcase 3 failed.")


    def testcase_04(self):
        a = AndGate(2)
        a.set_input(0,True)
        a.set_input(1,True)
        a.execute()
        self.assertEqual(True, a.Output[0], "Class AndGate Testcase 4 failed.")

    def testcase_05(self):
        a = AndGate(3)
        self.assertEqual(False, a.Output[0], "Class AndGate Testcase 5 failed.")
        self.assertEqual(False, a.Input[0], "Class AndGate Testcase 5 failed.")
        self.assertEqual(False, a.Input[1], "Class AndGate Testcase 5 failed.")
        self.assertEqual(False, a.Input[2], "Class AndGate Testcase 5 failed.")

    def testcase_06(self):
        a = AndGate(3)
        a.set_input(0,False)
        a.set_input(1,False)
        a.set_input(2,False)
        a.execute()
        self.assertEqual(False, a.Output[0], "Class AndGate Testcase 6 failed.")


    def testcase_07(self):
        a = AndGate(3)
        a.set_input(0,False)
        a.set_input(1,True)
        a.set_input(2,False)
        a.execute()
        self.assertEqual(False, a.Output[0], "Class AndGate Testcase 7 failed.")


    def testcase_08(self):
        a = AndGate(3)
        a.set_input(0,True)
        a.set_input(1,False)
        a.set_input(2,True)
        a.execute()
        self.assertEqual(False, a.Output[0], "Class AndGate Testcase 8 failed.")


    def testcase_09(self):
        a = AndGate(3)
        a.set_input(0,True)
        a.set_input(1,True)
        a.set_input(2,True)
        a.execute()
        self.assertEqual(True, a.Output[0], "Class AndGate Testcase 9 failed.")


class OrGateTest(unittest.TestCase):
    def testcase_00(self):
        a = OrGate(2)
        self.assertEqual(False, a.Output[0], "Class OrGate Testcase 0 failed.")
        self.assertEqual(False, a.Input[0], "Class OrGate Testcase 0 failed.")
        self.assertEqual(False, a.Input[1], "Class OrGate Testcase 0 failed.")

    def testcase_01(self):
        a = OrGate(2)
        a.set_input(0,False)
        a.set_input(1,False)
        a.execute()
        self.assertEqual(False, a.Output[0], "Class OrGate Testcase 1 failed.")

    def testcase_02(self):
        a = OrGate(2)
        a.set_input(0,False)
        a.set_input(1,True)
        a.execute()
        self.assertEqual(True, a.Output[0], "Class OrGate Testcase 2 failed.")

    def testcase_03(self):
        a = OrGate(2)
        a.set_input(0,True)
        a.set_input(1,False)
        a.execute()
        self.assertEqual(True, a.Output[0], "Class OrGate Testcase 3 failed.")

    def testcase_04(self):
        a = OrGate(2)
        a.set_input(0,True)
        a.set_input(1,True)
        a.execute()
        self.assertEqual(True, a.Output[0], "Class OrGate Testcase 4 failed.")

    def testcase_05(self):
        a = OrGate(4)
        self.assertEqual(False, a.Output[0], "Class OrGate Testcase 5 failed.")
        self.assertEqual(False, a.Input[0], "Class OrGate Testcase 5 failed.")
        self.assertEqual(False, a.Input[1], "Class OrGate Testcase 5 failed.")
        self.assertEqual(False, a.Input[2], "Class OrGate Testcase 5 failed.")
        self.assertEqual(False, a.Input[3], "Class OrGate Testcase 5 failed.")

    def testcase_06(self):
        a = OrGate(4)
        a.set_input(0,False)
        a.set_input(1,False)
        a.set_input(2,False)
        a.set_input(3,False)
        a.execute()
        self.assertEqual(False, a.Output[0], "Class OrGate Testcase 6 failed.")

    def testcase_07(self):
        a = OrGate(4)
        a.set_input(0,False)
        a.set_input(1,True)
        a.set_input(2,False)
        a.set_input(3,False)
        a.execute()
        self.assertEqual(True, a.Output[0], "Class OrGate Testcase 7 failed.")

    def testcase_08(self):
        a = OrGate(4)
        a.set_input(0,True)
        a.set_input(1,False)
        a.set_input(2,True)
        a.set_input(3,True)
        a.execute()
        self.assertEqual(True, a.Output[0], "Class OrGate Testcase 8 failed.")


    def testcase_09(self):
        a = OrGate(4)
        a.set_input(0,True)
        a.set_input(1,True)
        a.set_input(2,False)
        a.set_input(3,True)
        a.execute()
        self.assertEqual(True, a.Output[0], "Class OrGate Testcase 9 failed.")

class NandGateTest(unittest.TestCase):
    def testcase_00(self):
        a = NandGate(2)
        self.assertEqual(True, a.Output[0], "Class NandGate Testcase 0 failed.")
        self.assertEqual(False, a.Input[0], "Class NandGate Testcase 0 failed.")
        self.assertEqual(False, a.Input[1], "Class NandGate Testcase 0 failed.")

    def testcase_01(self):
        a = NandGate(2)
        a.set_input(0,False)
        a.set_input(1,False)
        a.execute()
        self.assertEqual(True, a.Output[0], "Class NandGate Testcase 1 failed.")

    def testcase_02(self):
        a = NandGate(2)
        a.set_input(0,False)
        a.set_input(1,True)
        a.execute()
        self.assertEqual(True, a.Output[0], "Class NandGate Testcase 2 failed.")

    def testcase_03(self):
        a = NandGate(2)
        a.set_input(0,True)
        a.set_input(1,False)
        a.execute()
        self.assertEqual(True, a.Output[0], "Class NandGate Testcase 3 failed.")

    def testcase_04(self):
        a = NandGate(2)
        a.set_input(0,True)
        a.set_input(1,True)
        a.execute()
        self.assertEqual(False, a.Output[0], "Class NandGate Testcase 4 failed.")

    def testcase_05(self):
        a = NandGate(4)
        self.assertEqual(True, a.Output[0], "Class NandGate Testcase 5 failed.")
        self.assertEqual(False, a.Input[0], "Class NandGate Testcase 5 failed.")
        self.assertEqual(False, a.Input[1], "Class NandGate Testcase 5 failed.")
        self.assertEqual(False, a.Input[2], "Class NandGate Testcase 5 failed.")
        self.assertEqual(False, a.Input[3], "Class NandGate Testcase 5 failed.")

    def testcase_06(self):
        a = NandGate(4)
        a.set_input(0,False)
        a.set_input(1,False)
        a.set_input(2,False)
        a.set_input(3,False)
        a.execute()
        self.assertEqual(True, a.Output[0], "Class NandGate Testcase 6 failed.")

    def testcase_07(self):
        a = NandGate(4)
        a.set_input(0,False)
        a.set_input(1,True)
        a.set_input(2,True)
        a.set_input(3,False)
        a.execute()
        self.assertEqual(True, a.Output[0], "Class NandGate Testcase 7 failed.")


    def testcase_08(self):
        a = NandGate(4)
        a.set_input(0,True)
        a.set_input(1,False)
        a.set_input(2,False)
        a.set_input(3,False)
        a.execute()
        self.assertEqual(True, a.Output[0], "Class NandGate Testcase 8 failed.")


    def testcase_09(self):
        a = NandGate(4)
        a.set_input(0,True)
        a.set_input(1,True)
        a.set_input(2,True)
        a.set_input(3,True)
        a.execute()
        self.assertEqual(False, a.Output[0], "Class NandGate Testcase 9 failed.")


class XORGateTest(unittest.TestCase):
    
    def testcase_00(self):
        a = XORGate(2)
        self.assertEqual(False, a.Output[0], "Class XORGate Testcase 0 failed.")
        self.assertEqual(False, a.Input[0], "Class XORGate Testcase 0 failed.")
        self.assertEqual(False, a.Input[1], "Class XORGate Testcase 0 failed.")

    def testcase_01(self):
        a = XORGate(2)
        a.set_input(0,False)
        a.set_input(1,False)
        a.execute()
        self.assertEqual(False, a.Output[0], "Class XORGate Testcase 1 failed.")

    def testcase_02(self):
        a = XORGate(2)
        a.set_input(0,False)
        a.set_input(1,True)
        a.execute()
        self.assertEqual(True, a.Output[0], "Class XORGate Testcase 2 failed.")

    def testcase_03(self):
        a = XORGate(2)
        a.set_input(0,True)
        a.set_input(1,False)
        a.execute()
        self.assertEqual(True, a.Output[0], "Class XORGate Testcase 3 failed.")

    def testcase_04(self):
        a = XORGate(2)
        a.set_input(0,True)
        a.set_input(1,True)
        a.execute()
        self.assertEqual(False, a.Output[0], "Class XORGate Testcase 4 failed.")

    def testcase_05(self):
        a = XORGate(3)
        self.assertEqual(False, a.Output[0], "Class XORGate Testcase 5 failed.")
        self.assertEqual(False, a.Input[0], "Class XORGate Testcase 5 failed.")
        self.assertEqual(False, a.Input[1], "Class XORGate Testcase 5 failed.")
        self.assertEqual(False, a.Input[2], "Class XORGate Testcase 5 failed.")

    def testcase_06(self):
        a = XORGate(3)
        a.set_input(0,False)
        a.set_input(1,False)
        a.set_input(2,False)
        a.execute()
        self.assertEqual(False, a.Output[0], "Class XORGate Testcase 6 failed.")


    def testcase_07(self):
        a = XORGate(3)
        a.set_input(0,False)
        a.set_input(1,True)
        a.set_input(2,False)
        a.execute()
        self.assertEqual(True, a.Output[0], "Class XORGate Testcase 7 failed.")


    def testcase_08(self):
        a = XORGate(3)
        a.set_input(0,True)
        a.set_input(1,False)
        a.set_input(2,True)
        a.execute()
        self.assertEqual(False, a.Output[0], "Class XORGate Testcase 8 failed.")


    def testcase_09(self):
        a = XORGate(3)
        a.set_input(0,True)
        a.set_input(1,True)
        a.set_input(2,True)
        a.execute()
        self.assertEqual(True, a.Output[0], "Class XORGate Testcase 9 failed.")

class NorGateTest(unittest.TestCase):
    
    def testcase_00(self):
        a = NorGate(2)
        self.assertEqual(True, a.Output[0], "Class OrGate Testcase 0 failed.")
        self.assertEqual(False, a.Input[0], "Class OrGate Testcase 0 failed.")
        self.assertEqual(False, a.Input[1], "Class OrGate Testcase 0 failed.")

    def testcase_01(self):
        a = NorGate(2)
        a.set_input(0,False)
        a.set_input(1,False)
        a.execute()
        self.assertEqual(True, a.Output[0], "Class OrGate Testcase 1 failed.")

    def testcase_02(self):
        a = NorGate(2)
        a.set_input(0,False)
        a.set_input(1,True)
        a.execute()
        self.assertEqual(False, a.Output[0], "Class OrGate Testcase 2 failed.")

    def testcase_03(self):
        a = NorGate(2)
        a.set_input(0,True)
        a.set_input(1,False)
        a.execute()
        self.assertEqual(False, a.Output[0], "Class OrGate Testcase 3 failed.")

    def testcase_04(self):
        a = NorGate(2)
        a.set_input(0,True)
        a.set_input(1,True)
        a.execute()
        self.assertEqual(False, a.Output[0], "Class OrGate Testcase 4 failed.")

    def testcase_05(self):
        a = NorGate(4)
        self.assertEqual(True, a.Output[0], "Class OrGate Testcase 5 failed.")
        self.assertEqual(True, a.Input[0], "Class OrGate Testcase 5 failed.")
        self.assertEqual(True, a.Input[1], "Class OrGate Testcase 5 failed.")
        self.assertEqual(True, a.Input[2], "Class OrGate Testcase 5 failed.")
        self.assertEqual(True, a.Input[3], "Class OrGate Testcase 5 failed.")

    def testcase_06(self):
        a = NorGate(4)
        a.set_input(0,False)
        a.set_input(1,False)
        a.set_input(2,False)
        a.set_input(3,False)
        a.execute()
        self.assertEqual(True, a.Output[0], "Class OrGate Testcase 6 failed.")

    def testcase_07(self):
        a = NorGate(4)
        a.set_input(0,False)
        a.set_input(1,True)
        a.set_input(2,False)
        a.set_input(3,False)
        a.execute()
        self.assertEqual(False, a.Output[0], "Class OrGate Testcase 7 failed.")

    def testcase_08(self):
        a = NorGate(4)
        a.set_input(0,True)
        a.set_input(1,False)
        a.set_input(2,True)
        a.set_input(3,True)
        a.execute()
        self.assertEqual(False, a.Output[0], "Class OrGate Testcase 8 failed.")


    def testcase_09(self):
        a = NorGate(4)
        a.set_input(0,True)
        a.set_input(1,True)
        a.set_input(2,False)
        a.set_input(3,True)
        a.execute()
        self.assertEqual(False, a.Output[0], "Class OrGate Testcase 9 failed.")


if __name__ == "__main__":
    unittest.main()