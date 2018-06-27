from abc import ABC, abstractclassmethod
import types

__version__="3.1"
__author__= "Sebastian Bensing"

class ShowType(ABC):

    @ abstractclassmethod
    def show(self,Logfunc):
        pass

    def _boolToBinary(self, bool_values):
        v1 = []
        if type(bool_values) is list:
            v1 = bool_values
        else:
            v1.append(bool_values)
            v1.append(False)
        for i in range(len(v1)-1): 
            if v1[i]: 
                v1[i] = "1" 
            else: 
                v1[i] = "0" 
        v1 = v1[:-1]
        return v1 

    def _to_decimal(self,values):
        if type(values) is list:
            if values[0] == True or values[0] == False:
                values = self._boolToBinary(values)
        else:
            if values == True or values == False:
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

class Show_binear(ShowType):
    def show(self, Logfunc):
        cwidth = 50
        first_last = ''.ljust(cwidth, '-')
        format_string = "-- {{0:10}}: {{1:{0}}} --".format(cwidth - 18)

        print(first_last)
        print(format_string.format("Name", Logfunc.Name))
       ## if isinstance(Logfunc.input[0],types.listtype):


        for i in range(len(Logfunc.Input)):
            print(format_string.format("Eingabe "+str(i)+"", str(self._boolToBinary(Logfunc.Input[i])).replace("'","")))
        
        
        print(format_string.format("Output ", str(self._boolToBinary(Logfunc.Output)).replace("'","")))

        print(first_last)

class Show_decimal(ShowType):
    def show(self, Logfunc):
        cwidth = 50
        first_last = ''.ljust(cwidth, '-')
        format_string = "-- {{0:10}}: {{1:{0}}} --".format(cwidth - 18)

        print(first_last)
        print(format_string.format("Name", str(Logfunc.Name)))
        for i in range(len(Logfunc.Input)):
            print(format_string.format("Input "+str(i)+"", str(self._to_decimal(Logfunc.Input[i]))))
        
        print(format_string.format("Output", str(self._to_decimal(Logfunc.Output))))
        print(first_last)

class Show_picture(ShowType):
    def show(self, Logfunc):
        cwidth = 50
        first_last = ''.ljust(cwidth, '-')
        format_string = "-- {{0:10}}: {{1:{0}}} --".format(cwidth - 18)

        print(first_last)
        print(format_string.format("Name", str(Logfunc.Name)))
        for i in range(len(Logfunc.Input)):
            print(format_string.format("Input "+str(i)+"", str(self._to_decimal(Logfunc.Input[i]))))

        print(format_string.format("Output", str(self._to_decimal(Logfunc.Output))))
        print(first_last)
        Logfunc.picture()
        print("\n\n\n")


        

