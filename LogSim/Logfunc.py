from abc import ABC, abstractmethod
__version__ = '3.0'
__author__ = 'Sebastian Bensing (sebastian.bensing@students.tbs1.de)'


class LogFunc(ABC):
    """
    This class calculates the logical AND function.
    """
    def __init__(self,anzahl):
        self.__Input = []
        self.__Output = False
        self.__Name = "LogFunc"
        self.__Anzahl = anzahl
        self.execute()
        

    def __get_anzahl(self):
        return self.__Anzahl

    def __get_input(self):
        """
        Returns the value of the second input signal.
        :return: Input1
        """
        return self.__Input1

    def __get_output(self):
        """
        Returns the value of the output signal.
        :return: Output
        """
        return self.__Output

    def __get_name(self):
        """
        Returns the value of the name property.
        :return: Name
        """
        return self.__Name



    def __set_input(self, value):
        """
        Sets the value of the second input signal
        :param value: (bool) new value
        :return: None
        """
        isinstance(value, bool)
        self.__Input.append(value)

    def _set_output(self, value):
        """
        Sets the value of the output signal
        :param value: (bool) new value
        :return: None
        """
        isinstance(value, bool)
        self.__Output = value

    def __set_name(self, value):
        """
        Sets the value of the name property
        :param value: (string) new value
        :return: None
        """
        isinstance(value, str)
        self.__Name = value

    Name = property(__get_name, __set_name)
    Input = property(__get_input, __set_input)
    Output = property(__get_output, None)
    Anzahl = property(__get_anzahl,None)

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

    def execute(self):
        """
        Computes the result of the logical connection of the two inputs.
        :return: None
        """
        for i in self.Input:
            if i == True:
                self.Output = True
            

class AndGate(LogFunc):

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
            Output = True

        

class XORGate(LogFunc):
    def execute(self):
        y = 0
        for i in self.Input:
            if i == True:
                y = y+1
        if y == 1:
            Output == True



class NandGate(LogFunc):
    def execute(self):
        x = True
        for i in self.Input:
            if i == False:
                x = False
        if x == True:
            Output = False
        else:
            Output = True
