from abc import ABC, abstractclassmethod

__version__="3.1"
__author__= "Sebastian Bensing"

class ShowType(ABC):

    @ abstractclassmethod
    def show(self,Logfunc):
        pass

    def _boolToBinary(self, bool_values): 
        for i in range(len(bool_values)): 
            if bool_values[i]: 
                bool_values[i] = "1" 
            else: 
                bool_values[i] = "0" 
        return bool_values 

    def _to_decimal(self,values):
        if values[0] == True or values[0] == False:
            values = self._boolToBinary(values)
        values2=0
        for i in range(len(values)):
            values2 = values2 + int(values[i])*(2**i)
        return values2

class ShowGate(ShowType):

    def show(self, Logfunc):
        cwidth = 50
        first_last = ''.ljust(cwidth, '-')
        format_string = "-- {{0:10}}: {{1:{0}}} --".format(cwidth - 18)

        print(first_last)
        print(format_string.format("Name", Logfunc.Name))
        print(format_string.format("Input", str(Logfunc.Input)))
        print(format_string.format("Output", str(Logfunc.Output)))
        print(first_last)

class ShowHalfAdder(ShowType):
    def show(self, Logfunc):
        cwidth = 50
        first_last = ''.ljust(cwidth, '-')
        format_string = "-- {{0:10}}: {{1:{0}}} --".format(cwidth - 18)

        print(first_last)
        print(format_string.format("Name", Logfunc.Name))
        print(format_string.format("Eingabe 1", str(self._boolToBinary(Logfunc.Input[0])).replace("'","")))
        print(format_string.format("Eingabe 2", str(self._boolToBinary(Logfunc.Input[1])).replace("'","")))
        print(format_string.format("Output 1", str(self._boolToBinary(Logfunc.Output[0])).replace("'","")))
        print(format_string.format("Output 2", str(self._boolToBinary(Logfunc.Output[1])).replace("'","")))
        print(first_last)

class Show_decimal(ShowType):
    def show(self, Logfunc):
        cwidth = 50
        first_last = ''.ljust(cwidth, '-')
        format_string = "-- {{0:10}}: {{1:{0}}} --".format(cwidth - 18)

        print(first_last)
        print(format_string.format("Name", str(Logfunc.Name)))
        for i in range(len(Logfunc.Input)):
            v1 = []
            v1.append(Logfunc.Input[i])
            v1.append(False)
            print(format_string.format("Input "+str(i)+"", str(self._to_decimal(v1))))
        
        print(format_string.format("Output", str(self._to_decimal(Logfunc.Output))))
        print(first_last)

class Show_eightbitadder(ShowType):
    def show(self, Logfunc):
        cwidth = 50
        first_last = ''.ljust(cwidth, '-')
        format_string = "-- {{0:10}}: {{1:{0}}} --".format(cwidth - 18)

        print(first_last)
        print(format_string.format("Name", str(Logfunc.Name)))

        for i in range(2):
            print(format_string.format("Input "+str(i)+"", str(self._to_decimal(Logfunc.Input[i]))))
        
        print(format_string.format("Output", str(self._to_decimal(Logfunc.Output))))
        print(first_last)
