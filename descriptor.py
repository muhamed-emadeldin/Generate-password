'''
Here we write a descriptor class for each attr in core class
@author:Muhamed ElSyaed
3-02-2021
''' 

import re
#--> create descriptor for name field
class NameCheck:
    def __init__(self, parameter, expected_type):
        self.parameter = parameter
        self.expected_type = expected_type

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.parameter]

    def __set__(self, instance, value):
        
        if len(value) < 1 or value == '':
            raise ValueError("The name of a platform should not empty.")
        if not isinstance(value, self.expected_type):
            raise TypeError(f"{self.expected_type} value is expected")
        instance.__dict__[self.parameter] = value


#--> Create descriptor for email feild
class EmailCheck:

    def __init__(self, parameter, expected_type):
        self.parameter      = parameter
        self.expected_type  = expected_type

    def __get__(self, instance, cls):
        if instance is None:
            return self
        return instance.__dict__[self.parameter]

    def __set__(self, instance, value):
        #-->basic variables
        pattern = '^([\w \d \. \_ \-]*)([\@])([\w \d \.]*)$'
        match   = re.search(pattern, value)

        if not match:
            raise ValueError('Email is invalid.')

        if not isinstance(value, self.expected_type):
            raise TypeError(f"{self.expected_type} value is expected")
        instance.__dict__[self.parameter] = value



