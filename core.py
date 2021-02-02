'''
Here we write a mian class to create automation password
@author:Muhamed ElSyaed
31-01-2021
''' 

import random
import secrets

#-->Validation
from decoratores import nameAssert, emailAssert

@nameAssert(name=str)
@emailAssert(email=str)
class ChangePassword(object):
  '''
  We start to create our args:[name, email, length of password, peirod to refresh password]
  --> create method to reverse and make a random letter is capital.
  --> create method to get defference between length of name and length of password.
  --> create method to get random numbers with length of defference.
  --> get symbol charatcter from list pun.
  --> generate password.
  '''
  #--> create initial method
  def __init__(self, name, email, leng, days):
    self.name     = name
    self.email    = email
    self.leng     = leng
    self.days     = days
    self.__pun    = ["!","#","$","%","&","*","+","-","/",":",";","<","=",">","?","@"]
    self.__ls     = []

  #--> create method to reverse and make a random letter is capital
  @property
  def reverse_random_capital(self):
    reverseName = self.name[::-1]
    captLetter  = random.sample(reverseName, 1)
    finalName   = reverseName.replace(captLetter[0], captLetter[0].upper(), 1)
    self.__ls.append(finalName)

  #--> create method to get defference between length of name and length of password
  @property
  def get_deference(self):
    return abs(len(self.name) - self.leng) - 1

  #--> create method to get random numbers with length of defference
  @property
  def random_digits(self):
    n     = self.get_deference
    start = 10 ** (n - 1)
    end   = (10 ** n) -1
    digit = random.randint(start, end)
    self.__ls.append(str(digit))

  #--> get symbol charatcter from list pun
  @property
  def get_symbol(self):
    symbol  = secrets.choice(self.__pun)
    self.__ls.append(symbol)

  #--> generate password
  @property
  def generate_pass(self):
    self.reverse_random_capital
    self.random_digits
    self.get_symbol

    passWord  = random.sample(self.__ls, len(self.__ls))
    return "".join(passWord)


  #--> create call method
  def __call__(self):
    return self.generate_pass

  