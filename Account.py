class Account:

    account_list = []
    account_id_list = []

    def __init__(self,id,balance,time_stamp,owner=None):
        balance = int(balance)
        if balance >= 0:
            self.id = id
            self.balance = balance
            self.time_stamp = time_stamp
            self.owner = owner
            Account.account_list.append(self)
            # Account.account_id_list.append(self.id)
        else:
            return("Please deposit more funds to create an account.")   

    def withdraw(self,withdraw_amount):
        if withdraw_amount > self.balance:
            return ("Not enough funds to complete transaction.")
        else:
            self.balance -= self.withdraw_amount
            return self.balance

    def deposit(self,deposit_amount):
        self.balance += self.deposit_amount
        return self.balance

    def current_balance(self):
        return self.balance

    def all_acounts(self):
        return Account.account_list

    def find(self,account_id):
        for item in Account.account_list:
            if item.id == account_id:
                return item

# try:
#     with open("./support/accounts.csv") as accounts:
        
#         account_line = csv.reader(accounts)
        
#         for x in account_line: 
#             new_account = Account(*x)

#     with open("./support/account_owners.csv") as owned_accounts:

#         owned_account_line = csv.reader(owned_accounts)  
#         for account_id in owned_account_line:
#             if account_id[0] in Account.account_id_list:
#                 current_account_index = Account.account_id_list.index(account_id[0])
#                 current_account = Account.account_list[current_account_index]
#                 current_account.owner = account_id[1]
#                 print(current_account.__dict__)
            

# except:
#     print('not working')


# nathan = Account(1234,1000,"1999-02-12 14:03:00 -0800")

# print(nathan.find(1234).__dict__)


# print(Account.all_acounts(Account))

    