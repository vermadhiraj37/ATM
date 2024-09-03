#constructor(special function)->superpower ->

class Atm:
  def __init__(self):
    self.pin = ''
    self.balance = 0
    self.load()

  def load(self):
      print('Create an ATM pin ')
      self.create_pin()

  def menu(self):
    user_input = input("""
    Hi how can I help you?
    1. Press 1 to Change pin
    2. Press 2 to Check balance
    3. Press 3 to Withdraw
    4. Press anything else to Exit
    """)

    if user_input == '1':
      self.change_pin()
    elif user_input == '2':
      self.check_balance()
    elif user_input == '3':
      self.withdraw()
    else:
      exit()

  def create_pin(self):
    user_pin = input('Enter a 4 digit pin ')
    self.pin = user_pin

    user_balance = int(input('Enter balance '))
    self.balance = user_balance

    print('Pin created successfully')
    self.menu()

  def change_pin(self):
    old_pin = input('Enter old pin ')

    if old_pin == self.pin:
      # let him change the pin
      new_pin = input('Enter new pin ')
      self.pin = new_pin
      print('Pin changed successfully')

    else:
      print('Enter correct old pin')
    self.menu()

  def check_balance(self):
    user_pin = input('Enter your pin ')
    if user_pin == self.pin:
      print('Your balance is ',self.balance)
    else:
      print('Enter correct pin')
    self.menu()

  def withdraw(self):
    user_pin = input('Enter the pin ')
    if user_pin == self.pin:
      # allow to withdraw
      amount = int(input('Enter the amount to withdraw '))
      if amount <= self.balance:
        self.balance = self.balance - amount
        print('Withdrawl successful. Your balance is',self.balance)
      else:
        print('Low balance.Your balance is',self.balance)
    else:
      print('Enter correct pin')
    self.menu()
obj=Atm()