import csv

from Account import Account
from Owner import Owner

try:
    with open("./support/accounts.csv") as accounts:
        
        account_line = csv.reader(accounts)
        
        for x in account_line: 
            new_account = Account(*x)

    with open("./support/owners.csv") as owner:
        
        owner_line = csv.reader(owner)
        
        for x in owner_line: 
            new_owner = Owner(*x)

    with open("./support/account_owners.csv") as owned_accounts:

        owned_account_line = csv.reader(owned_accounts)  
        for owner_id in owned_account_line:
            if owner_id[1] in Owner.owner_id_list:
                # current_owner_list = Owner.owner_id_list.index(owner_id[1])
                current_owner_index = Owner.owner_id_list.index(owner_id[1])
                print('working until here')
                current_owner = Owner.owner_list[current_owner_index]
                current_owner.account = owner_id[0]
                print(current_owner.__dict__)
                
except:
    print('not working')

for owner in Owner.owner_list:
    print(f"Name: {owner.first_name} {owner.last_name}, Account Number : {owner.account}")


#  with open("./support/account_owners.csv") as owned_accounts:

#         owned_account_line = csv.reader(owned_accounts)  
#         for account_id in owned_account_line:
#             if account_id[0] in Account.account_id_list:
#                 current_account_index = Account.account_id_list.index(account_id[0])
#                 current_account = Account.account_list[current_account_index]
#                 current_account.owner = account_id[1]
#                 print(current_account.__dict__)

#             if account_id[1] in Owner.owner_list:

class Savings(Account):
    def __init__(self,balance,time_stamp,owner=None):
        if balance >= 10.00:
            super.__init__(balance,time_stamp,owner)


