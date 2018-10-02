class BankAccount(object):
    def __init__(self):
        pass

    def get_balance(self):
        pass

    def open(self):
        pass

    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass

    def close(self):
        pass

# Simulate a bank account supporting opening/closing, withdrawals, and deposits of 
# money. Watch out for concurrent transactions!
#
# A bank account can be accessed in multiple ways. Clients can make deposits and
# withdrawals using the internet, mobile phones, etc. Shops can charge against the account.
#
# Create an account that can be accessed from multiple threads/processes
# (terminology depends on your programming language).
#
# It should be possible to close an account; operations against a closed account must fail.
