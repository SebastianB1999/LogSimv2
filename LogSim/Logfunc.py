from abc import ABC, abstractmethod
__version__ = '3.0'
__author__ = 'Sebastian Bensing (sebastian.bensing@students.tbs1.de)'


class LogFunc(ABC):
    """
    This class calculates the logical AND function.
    """
    def __init__(self,Eingänge,Ausgänge):
        self.__Output = []
        self.__Name = "LogFunc"
        self.__Anzahl = Eingänge
        self.__Ausgänge = Ausgänge
        self.__Input = []
        for i in range(Eingänge):
            self.__Input.append(False)
        for i in range(Ausgänge):
            self.__Output.append(False)
        self.execute()
        

    def __get_anzahl(self):
        return self.__Anzahl

    def __get_input(self):
        """
        Returns the value of the second input signal.
        :return: Input1
        """
        return self.__Input
        """
        Returns the value of the name property.
        :return: Name

    def __get_output(self):
    #    """
     #   Returns the value of the output signal.
      #  :return: Output
       # """
        return self.__Output

    def __get_name(self):
      #  """
        return self.__Name



    def set_input(self,position ,value):
        """
        Sets the value of the second input signal
        :param value: (bool) new value
        :return: None
        """
        isinstance(value, bool)
        isinstance(position,int)
        if position >= 0:
            self.__Input[position] = value

    def _set_output(self, value):
        """
        Sets the value of the output signal
        :param value: (bool) new value
        :return: None
        """
        isinstance(value, bool)
        x = self.__Ausgänge
        for i in range(self.__Ausgänge):
            self.__Output[i] = value

    def __set_name(self, value):
        """
        Sets the value of the name property
        :param value: (string) new value
        :return: None
        """
        isinstance(value, str)
        self.__Name = value

    Name = property(__get_name, __set_name)
    Output = property(__get_output, None)
    Anzahl = property(__get_anzahl,None)
    Input = property(__get_input,set_input)

    def __str__(self):
        """
        Converts the status of the object to a string. The function will be called
        implicitly when you try to convert the object in a string.
        :return: Printable string of the status.
        """
        status = type(self).__name__ + "." + self.Name + ": "
        status += "(" + str(self.Input0) + "," + str(self.Input1) + ") "
        status += "-> (" + str(self.Output) + ")"
        return status

    def show(self):
        """
        Shows the value of each property of the class and the class name.
        :return: None
        """
        cwidth = 50
        first_last = ''.ljust(cwidth, '-')
        format_string = "-- {{0:10}}: {{1:{0}}} --".format(cwidth - 18)

        print(first_last)
        print(format_string.format("Name", self.Name))
        print(format_string.format("Type", type(self).__name__))
        print(format_string.format("Input0", str(self.Input0)))
        print(format_string.format("Input1", str(self.Input1)))
        print(format_string.format("Output", str(self.Output)))
        print(first_last)

    @abstractmethod
    def execute(self):
        raise NotImplementedError
        #pass



class OrGate(LogFunc):
    def __init__(self, Eing):
        return super().__init__(Eing, 1)

    def execute(self):
        """
        Computes the result of the logical connection of the two inputs.
        :return: None
        """
        for i in self.Input:
            if i == True:
                self._set_output(True)
            

class AndGate(LogFunc):
    def __init__(self, Eing):
        return super().__init__(Eing, 1)

    def execute(self):
        """
        Computes the result of the logical connection of the two inputs.
        :return: None
        """
        x = True
        for i in self.Input:
            if i == False:
                x = False
        if x == True:
            self._set_output(True)

        

class XORGate(LogFunc):
    def __init__(self, Eing):
        return super().__init__(Eing, 1)

    def execute(self):# wenn eine ungrade anzahl an true gibt ist das ergebnis true
        y = 0
        for i in self.Input:
            if i == True:
                y = y+1
        if y == 1:
            self._set_output(True)
        if y%2 ==1:
            self._set_output(True)



class NandGate(LogFunc):
    def __init__(self, Eing):
        return super().__init__(Eing, 1)

    def execute(self):
        x = True
        for i in self.Input:
            if i == False:
                x = False
        if x == True:
            self._set_output(False)
        else:
            self._set_output(True)

# Nor muss noch implementiert werden

 