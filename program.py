from core import ChangePassword

if __name__ == '__main__':
  name      = input('Please enter the name of the platform on which you want to generate a password. \n')
  email     = input('Please Enter your email. \n')
  password  = ChangePassword(name=name, email=email, leng=9, days=9)
  password()