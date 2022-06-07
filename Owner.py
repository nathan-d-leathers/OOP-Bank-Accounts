class Owner:

    owner_list = []
    owner_id_list = []

    def __init__(self,id,last_name,first_name,street_address,city,state,account=0):
        self.id = id
        self.last_name = last_name
        self.first_name = first_name
        self.street_address = street_address
        self.city = city
        self.state = state
        self.account = account
        Owner.owner_list.append(self)
        Owner.owner_id_list.append(self.id)


# try:
#     with open("./support/owners.csv") as owner:
        
#         owner_line = csv.reader(owner)
        
#         for x in owner_line: 
#             new_owner = Owner(*x)
            
# except:
#     print('not working')

# print(Owner.owner_list)


