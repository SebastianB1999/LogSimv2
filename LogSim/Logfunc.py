from abc import ABC, abstractmethod
import copy

__version__ = '3.0'
__author__ = 'Sebastian Bensing (sebastian.bensing@students.tbs1.de)'


class LogFunc(ABC):
    """
    abstract base class for the logical functions
    """
    def __init__(self,Eingänge,Ausgänge,bits=None):
        self.__Output = []
        self.__Name = type(self).__name__
        self.__Anzahl = Eingänge
        self.__Ausgänge = Ausgänge
        self.__Input = []
        if bits is None:
            for i in range(Eingänge):
                self.__Input.append(False)
        else:
            for i in range(Eingänge):
                v1 = []
                for x in range(bits):
                    v1.append(False)
                self.__Input.append(v1)

        for i in range(Ausgänge):
            self.__Output.append(False)
        self.execute()
        

    def __get_anzahl(self):
        # return the number of inputs
        return self.__Anzahl

    def __get_input(self):
        # return the list Input
        return self.__Input


    def __get_output(self):
        # return the list Output
        return self.__Output

    def __get_name(self):
        # return the string name
        return self.__Name



    def set_input(self,position ,value):
        #Sets the value of the Input at a specified position
        
        isinstance(value, bool)
        isinstance(position,int)
        if position >= 0:
            self.__Input[position] = value

    def _set_output(self,position, value):
        # Sets the value of Output at a specified position
        isinstance(value, bool)
        isinstance(position,int)
        if position >= 0:
            self.__Output[position] = value

    def __set_name(self, value):
        # Sets the value of Name
        isinstance(value, str)
        self.__Name = value

    # Properties
    Name = property(__get_name, __set_name)
    Output = property(__get_output, None)
    Anzahl = property(__get_anzahl,None)
    Input = property(__get_input,set_input)

    def __str__(self):
        # Converts the status of the object to a string.
        status = type(self).__name__ + "." + self.Name + ": "
        status += "(" + str(self.Input)+") "
        status += "-> (" + str(self.Output) + ")"
        return status

    def show(self):
        # Shows the value of each property of the class and the class name.
        cwidth = 50
        first_last = ''.ljust(cwidth, '-')
        format_string = "-- {{0:10}}: {{1:{0}}} --".format(cwidth - 18)

        print(first_last)
        print(format_string.format("Name", self.Name))
        print(format_string.format("Type", type(self).__name__))
        print(format_string.format("Input0", str(self.Input)))
        print(format_string.format("Output", str(self.Output)))
        print(first_last)

    @abstractmethod
    def execute(self):
        # Abstract method for calculate Output of the logical function
        raise NotImplementedError
        #pass



class OrGate(LogFunc):
    # Class calculates the Or Gate
    def __init__(self, Eing):
        return super().__init__(Eing, 1)


    def execute(self):
    # Calculation of the output based on the inputs
        self._set_output(0,False)
        for i in self.Input:
            if i == True:
                self._set_output(0,True)
            

class AndGate(LogFunc):
    # Class calculates the And Gate
    def __init__(self, Eing):
        return super().__init__(Eing, 1)
        

    def execute(self):
        # Calculation of the output based on the inputs
        self._set_output(0,False)
        x = True
        for i in self.Input:
            if i == False:
                x = False
        if x == True:
            self._set_output(0,True)

        

class XORGate(LogFunc):
    # Class calculates the XOr Gate
    def __init__(self, Eing):
        return super().__init__(Eing, 1)
        

    def execute(self):
        # Calculation of the output based on the inputs
        y = 0
        self._set_output(0,False)
        for i in self.Input:
            if i == True:
                y = y+1
        if y == 1:
            self._set_output(0,True)
        if y%2 ==1:
            self._set_output(0,True)



class NandGate(LogFunc):
    # Class calculates the NAnd Gate
    def __init__(self, Eing):
        return super().__init__(Eing, 1)
        

    def execute(self):
        # Calculation of the output based on the inputs
        x = True
        for i in self.Input:
            if i == False:
                x = False
        if x == True:
            self._set_output(0,False)
        else:
            self._set_output(0,True)


class NorGate(LogFunc):
    # Class calculates the NOr Gate
    def __init__(self, Eing):
        return super().__init__(Eing, 1)
        

    def execute(self):
        # Calculation of the output based on the inputs
        self._set_output(0,True)
        for i in self.Input:
            if i == True:
                self._set_output(0,False)
            

class NotGate(LogFunc):
    # Class calculates the Not Gate
    def __init__(self, Eing):
        return super().__init__(Eing, Eing)
        

    def execute(self):
        # Calculation of the output based on the inputs
        v1 = 0
        for i in self.Input:
            if i == True:
                self._set_output(v1, False)
            else:
                self._set_output(v1, True)
            v1 = v1 +1

class HalfAdder(LogFunc):
    # Class calculates the HalfAdder
    def __init__(self):
        self.__andgate = AndGate(2)
        self.__xorgate = XORGate(2)
        return super().__init__(2, 2)
        
    
    def execute(self):
       # Calculation of the output based on the inputs
       self.__andgate.set_input(0,self.Input[0])
       self.__andgate.set_input(1,self.Input[1])
       self.__andgate.execute()
       self._set_output(1,self.__andgate.Output[0])
       
       
       self.__xorgate.set_input(0,self.Input[0])
       self.__xorgate.set_input(1,self.Input[1])
       self.__xorgate.execute()
       self._set_output(0,self.__xorgate.Output[0])
       
class Fulladder(LogFunc):
    # Class calculates the FullAdder
    def __init__(self):
        self.__halfadder1 = HalfAdder()
        self.__orgate = OrGate(2)
        return super().__init__(3, 2)
        

    def execute(self):
        # Calculation of the output based on the inputs
        self.__halfadder1.set_input(0,self.Input[0])
        self.__halfadder1.set_input(1,self.Input[1])
        self.__halfadder1.execute()
        v1 = self.__halfadder1.Output[0]
        v2 = self.__halfadder1.Output[1]
        
        self.__halfadder1.set_input(0,v1)
        self.__halfadder1.set_input(1,self.Input[2])
        self.__halfadder1.execute()
        v3 = self.__halfadder1.Output[0]
        v4 = self.__halfadder1.Output[1]
        
        self._set_output(0,v3)

        self.__orgate.set_input(0,v2)
        self.__orgate.set_input(1,v4)
        self.__orgate.execute()
        v5 = self.__orgate.Output[0]
        self._set_output(1,v5)

class eightbitadder(LogFunc):
    # class calculates the result of two 8-bit numbers
    def __init__(self):
        self.__halfadder = HalfAdder()
        self.__fulladder = Fulladder()
        return super().__init__(2,9,8)

 #   def __init__(self,bits):
  #      self.__halfadder = HalfAdder()
   #     self.__fulladder = Fulladder()
    #    return super().__init__(2,bits, bits+1)

    def execute(self):
        # Calculation of the output based on the inputs
        self.__halfadder.set_input(0,self.Input[0][0])
        self.__halfadder.set_input(1,self.Input[1][0])
        self.__halfadder.execute()
        v1 = self.__halfadder.Output[0]
        v2 = self.__halfadder.Output[1]
        self._set_output(0,v1)
        x=1
        while x < len(self.Input[0]):
            self.__fulladder.set_input(0,self.Input[0][x])
            self.__fulladder.set_input(1,self.Input[1][x])
            self.__fulladder.set_input(2,v2)
            self.__fulladder.execute()
            v3 = self.__fulladder.Output[0]
            v2 = self.__fulladder.Output[1]
            self._set_output(x,v3)
            x = x + 1
        self._set_output(x,v2)
        v=0

