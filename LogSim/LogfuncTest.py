import unittest
from Logfunc import AndGate
from Logfunc import OrGate
from Logfunc import NandGate
from Logfunc import XORGate
from Logfunc import NorGate
from Logfunc import HalfAdder
from Logfunc import Fulladder
from Logfunc import eightbitadder


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
        self.assertEqual(False, a.Input[0], "Class OrGate Testcase 5 failed.")
        self.assertEqual(False, a.Input[1], "Class OrGate Testcase 5 failed.")
        self.assertEqual(False, a.Input[2], "Class OrGate Testcase 5 failed.")
        self.assertEqual(False, a.Input[3], "Class OrGate Testcase 5 failed.")

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

class HalfAdderTest(unittest.TestCase):
    
    def testcase_00(self):
        a = HalfAdder()
        self.assertEqual(False, a.Output[0], "Class HalfAdder Testcase 0 failed.")
        self.assertEqual(False, a.Output[1], "Class HalfAdder Testcase 0 failed.")
        self.assertEqual(False, a.Input[0], "Class HalfAdder Testcase 0 failed.")
        self.assertEqual(False, a.Input[1], "Class HalfAdder Testcase 0 failed.")

    def testcase_01(self):
        a = HalfAdder()
        a.set_input(0,False)
        a.set_input(1,False)
        a.execute()
        self.assertEqual(False, a.Output[0], "Class HalfAdder Testcase 1 failed.")
        self.assertEqual(False, a.Output[1], "Class HalfAdder Testcase 1 failed.")

    def testcase_02(self):
        a = HalfAdder()
        a.set_input(0,False)
        a.set_input(1,True)
        a.execute()
        self.assertEqual(True, a.Output[0], "Class HalfAdder Testcase 2 failed.")
        self.assertEqual(False, a.Output[1], "Class HalfAdder Testcase 2 failed.")

    def testcase_03(self):
        a = HalfAdder()
        a.set_input(0,True)
        a.set_input(1,False)
        a.execute()
        self.assertEqual(True, a.Output[0], "Class HalfAdder Testcase 3 failed.")
        self.assertEqual(False, a.Output[1], "Class HalfAdder Testcase 3 failed.")

    def testcase_04(self):
        a = HalfAdder()
        a.set_input(0,True)
        a.set_input(1,True)
        a.execute()
        self.assertEqual(False, a.Output[0], "Class HalfAdder Testcase 2 failed.")
        self.assertEqual(True, a.Output[1], "Class HalfAdder Testcase 2 failed.")


class FullAdderTest(unittest.TestCase):
    
    def testcase_00(self):
        a = Fulladder()
        self.assertEqual(False, a.Output[0], "Class Fulladder Testcase 0 failed.")
        self.assertEqual(False, a.Output[1], "Class Fulladder Testcase 0 failed.")
        self.assertEqual(False, a.Input[0], "Class Fulladder Testcase 0 failed.")
        self.assertEqual(False, a.Input[1], "Class Fulladder Testcase 0 failed.")
        self.assertEqual(False, a.Input[2], "Class Fulladder Testcase 0 failed.")

    def testcase_01(self):
        a = Fulladder()
        a.set_input(0,False)
        a.set_input(1,False)
        a.set_input(2,False)
        a.execute()
        self.assertEqual(False, a.Output[0], "Class FullAdder Testcase 1 failed.")
        self.assertEqual(False, a.Output[1], "Class FullAdder Testcase 1 failed.")
        

    def testcase_02(self):
        a = Fulladder()
        a.set_input(0,False)
        a.set_input(1,False)
        a.set_input(2,True)
        a.execute()
        self.assertEqual(True, a.Output[0], "Class FullAdder Testcase 2 failed.")
        self.assertEqual(False, a.Output[1], "Class FullAdder Testcase 2 failed.")

    def testcase_03(self):
        a = Fulladder()
        a.set_input(0,False)
        a.set_input(1,True)
        a.set_input(2,False)
        a.execute()
        self.assertEqual(True, a.Output[0], "Class FullAdder Testcase 3 failed.")
        self.assertEqual(False, a.Output[1], "Class FullAdder Testcase 3 failed.")
       
    def testcase_04(self):
        a = Fulladder()
        a.set_input(0,False)
        a.set_input(1,True)
        a.set_input(2,True)
        a.execute()
        self.assertEqual(False, a.Output[0], "Class FullAdder Testcase 4 failed.")
        self.assertEqual(True, a.Output[1], "Class FullAdder Testcase 4 failed.")

    def testcase_05(self):
        a = Fulladder()
        a.set_input(0,True)
        a.set_input(1,False)
        a.set_input(2,False)
        a.execute()
        self.assertEqual(True, a.Output[0], "Class FullAdder Testcase 5 failed.")
        self.assertEqual(False, a.Output[1], "Class FullAdder Testcase 5 failed.")

    def testcase_06(self):
        a = Fulladder()
        a.set_input(0,True)
        a.set_input(1,False)
        a.set_input(2,True)
        a.execute()
        self.assertEqual(False, a.Output[0], "Class FullAdder Testcase 6 failed.")
        self.assertEqual(True, a.Output[1], "Class FullAdder Testcase 6 failed.")


    def testcase_07(self):
        a = Fulladder()
        a.set_input(0,True)
        a.set_input(1,True)
        a.set_input(2,False)
        a.execute()
        self.assertEqual(False, a.Output[0], "Class FullAdder Testcase 7 failed.")
        self.assertEqual(True, a.Output[1], "Class FullAdder Testcase 7 failed.")

    def testcase_08(self):
        a = Fulladder()
        a.set_input(0,True)
        a.set_input(1,True)
        a.set_input(2,True)
        a.execute()
        self.assertEqual(True, a.Output[0], "Class FullAdder Testcase 8 failed.")
        self.assertEqual(True, a.Output[1], "Class FullAdder Testcase 8 failed.")

class eightbitadderTest(unittest.TestCase):
    
    def testcase_01(self): 
        a = eightbitadder()
        testdatas = [
            [False, False, False, False, False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
            [True, False, False, False, False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False],
            [True, False, True, False, False,False,False,False,False,False,False,False,False,False,False,True,True,False,True,False,False,False,False,True,False],
            [True, False, False, False, False,False,False,False,True,False,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False],
            [True, False, False, True, False,False,False,False,     True,False,False,True,False,False,False,False,      False,True,False,False,True,False,False,False,False],
            [True, False, False, False, False,False,False,False,False,False,False,False,True,False,False,False,True,False,False,False,True,False,False,False,False],
            [True, True, True, True, True,True,True,True,False,False,False,False,False,False,False,True,True,True,True,True,True,True,True,False,True],
            [True, True, True, True, True,True,True,True,True,True,True,True,True,True,True,True,False,True,True,True,True,True,True,True,True],
        ]
        zähler = 1
        for testdata in testdatas:
            
            v1 = []
            for i in range(0, 8):
                v1.append(testdata[i])
            a.set_input(0,v1)
            v2 = []
            for i in range(8, 16):
                v2.append(testdata[i])
            a.set_input(1,v2)

            a.execute()
            self.assertEqual(testdata[16], a.Output[0], "Class eightbitadder Testcase 1 failed. Test: "+str(zähler))
            self.assertEqual(testdata[17], a.Output[1], "Class eightbitadder Testcase 1 failed. Test: "+str(zähler))
            self.assertEqual(testdata[18], a.Output[2], "Class eightbitadder Testcase 1 failed. Test: "+str(zähler))
            self.assertEqual(testdata[19], a.Output[3], "Class eightbitadder Testcase 1 failed. Test: "+str(zähler))
            self.assertEqual(testdata[20], a.Output[4], "Class eightbitadder Testcase 1 failed. Test: "+str(zähler))
            self.assertEqual(testdata[21], a.Output[5], "Class eightbitadder Testcase 1 failed. Test: "+str(zähler))
            self.assertEqual(testdata[22], a.Output[6], "Class eightbitadder Testcase 1 failed. Test: "+str(zähler))
            self.assertEqual(testdata[23], a.Output[7], "Class eightbitadder Testcase 1 failed. Test: "+str(zähler))
            self.assertEqual(testdata[24], a.Output[8], "Class eightbitadder Testcase 1 failed. Test: "+str(zähler))
            zähler = zähler +1





if __name__ == "__main__":
    unittest.main()