'''
Here we combiend descriptor with decorator
@author:Muhamed ElSyaed
3-02-2021
''' 

from descriptor import NameCheck, EmailCheck

def nameAssert(**kwargs):
    def decorate(cls):
      for parameter, expected_type in kwargs.items():
          setattr(cls, parameter, NameCheck(parameter, expected_type))
      return cls
    return decorate


def emailAssert(**kwargs):
  def decorator(cls):
    for parameter, expected_type in kwargs.items():
      setattr(cls, parameter, EmailCheck(parameter, expected_type))
    
    return cls
  
  return decorator


